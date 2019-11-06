
#include "HAlphaGAM.h"

OBJECTLOADREGISTER(HAlphaGAM, "$Id: $")


//  ******** Default constructor ***********************************
HAlphaGAM::HAlphaGAM(){
	this->SignalsInputInterface = NULL;
	this->SignalsOutputInterface = NULL;
}




// ********* Destructor ********************************************
HAlphaGAM::~HAlphaGAM()
{
//	if(this->SignalsInputInterface != NULL) delete[] this->SignalsInputInterface ;
//	if(this->SignalsOutputInterface != NULL) delete[] this->SignalsOutputInterface;
}



//{ ********* Initialise the module ********************************
bool HAlphaGAM::Initialise(ConfigurationDataBase& cdbData){
   
	CDBExtended cdb(cdbData);

	int i;

	if(!cdb.ReadInt32(usectime_to_wait_for_starting_operation, "usectime_to_wait_for_starting_operation"))
	{
		AssertErrorCondition(InitialisationError,"HAlphaGAM::Initialise: %s usectime_to_wait_for_starting_operation",this->Name());
		return False;
	}
	else AssertErrorCondition(Information,"HAlphaGAM::Initialise: usectime_to_wait_for_starting_operation = %d",usectime_to_wait_for_starting_operation);

//	sleep(3);
// Create the signal interfaces
	if(!AddInputInterface(this->SignalsInputInterface, "HAlphaGAMInputInterface"))
	{
		AssertErrorCondition(InitialisationError, "HAlphaGAM::Initialise: %s failed to add the TimewindowsGAMInputInterface", this->Name());
		return False;
	}
	if(!AddOutputInterface(this->SignalsOutputInterface, "HAlphaGAMOutputInterface"))
	{
		AssertErrorCondition(InitialisationError, "HAlphaGAM::Initialise: %s failed to add the TimewindowsGAMOutputInterface", this->Name());
		return False;
	}

//	INPUT SIGNALS (interface)
	if(!cdb->Move("input_signals"))
	{
		AssertErrorCondition(InitialisationError,"HAlphaGAM::Initialise: %s Could not move to \"input_signals\"",this->Name());
		return False;
	}
		int number_of_signals_to_read = 2;
		FString *CDB_move_to;
		FString *SignalType;
		CDB_move_to = new FString[number_of_signals_to_read];
		SignalType = new FString[number_of_signals_to_read];
		CDB_move_to[0].Printf("h_alfa_raw");
		CDB_move_to[1].Printf("time");
		for (i=0;i<number_of_signals_to_read;i++){
			
			if(!cdb->Move(CDB_move_to[i].Buffer()))
			{
				AssertErrorCondition(InitialisationError,"HAlphaGAM::Initialise: %s Could not move to \"%s\"",this->Name(),CDB_move_to[i].Buffer());
				return False;
			}
			
			if(cdb->Exists("SignalType"))
			{
				FString signalName;
				cdb.ReadFString(SignalType[i], "SignalType");
			}
			if(cdb->Exists("SignalName"))
			{
				FString SignalName;
				cdb.ReadFString(SignalName, "SignalName");
				AssertErrorCondition(Information,"HAlphaGAM::Initialise: Added signal = %s", SignalName.Buffer());
				
				if(!this->SignalsInputInterface->AddSignal(SignalName.Buffer(), SignalType[i].Buffer()))
				{
					AssertErrorCondition(InitialisationError,"HAlphaGAM::Initialise: %s failed to add signal", this->Name());
					return False;
				}
			}
			
			
			cdb->MoveToFather();
		}

	cdb->MoveToFather();


//	OUTPUT SIGNALS (interface)
	if(!cdb->Move("output_signals"))
	{
		AssertErrorCondition(InitialisationError,"HAlphaGAM::Initialise: %s Could not move to \"output_signals\"",this->Name());
		return False;
	}
	
		number_of_signals_to_read = 1;
		CDB_move_to = new FString[number_of_signals_to_read];
		SignalType = new FString[number_of_signals_to_read];
		CDB_move_to[0].Printf("h_alfa_output");
		for (i=0;i<number_of_signals_to_read;i++){
			
			if(!cdb->Move(CDB_move_to[i].Buffer()))
			{
				AssertErrorCondition(InitialisationError,"HAlphaGAM::Initialise: %s Could not move to \"%s\"",this->Name(),CDB_move_to[i].Buffer());
				return False;
			}
			
			if(cdb->Exists("SignalType"))
			{
				FString signalName;
				cdb.ReadFString(SignalType[i], "SignalType");
			}
			if(cdb->Exists("SignalName"))
			{
				FString SignalName;
				cdb.ReadFString(SignalName, "SignalName");
				AssertErrorCondition(Information,"HAlphaGAM::Initialise: Added signal = %s", SignalName.Buffer());
				
				if(!this->SignalsOutputInterface->AddSignal(SignalName.Buffer(), SignalType[i].Buffer()))
				{
					AssertErrorCondition(InitialisationError,"HAlphaGAM::Initialise: %s failed to add signal", this->Name());
					return False;
				}
			}
			cdb->MoveToFather();
		}

	cdb->MoveToFather();

		this->n_samples = 0;
		this->accumulator = 0;
		this->remove_offset = 0;

	return True;
}
//} ******************************************************************



//{ ********* Execute the module functionalities *******************
bool HAlphaGAM::Execute(GAM_FunctionNumbers functionNumber){

	InputInterfaceStruct *inputstruct = (InputInterfaceStruct *) this->SignalsInputInterface->Buffer();
	this->SignalsInputInterface->Read();
//	AssertErrorCondition(InitialisationError,"HAlphaGAM:: %s inputstruct = %f ",this->Name(), inputstruct[0].ADC_H_alpha);
	OutputInterfaceStruct *outputstruct = (OutputInterfaceStruct *) this->SignalsOutputInterface->Buffer();


	if(functionNumber == GAMOnline){
		// Determine the ADC offset
		if(inputstruct[0].usectime > 0 && inputstruct[0].usectime < usectime_to_wait_for_starting_operation){
			n_samples++;
				
			this->accumulator += (float) inputstruct[0].ADC_H_alpha;
			this->remove_offset = this->accumulator  / (float) this->n_samples;
			outputstruct[0].HAlfaOutput = 0;
		}
		else{
			//send offset corrections to logger once
			if (this->n_samples >0 ){

				AssertErrorCondition(Information,"HAlphaGAM::Execute: %s OFFSET = %f, number of samples = %d", this->Name(), this->remove_offset, n_samples);
				n_samples = 0;
			}

			outputstruct[0].HAlfaOutput = 100 * (inputstruct[0].ADC_H_alpha - remove_offset);
		} 
	}
	else {
		this->n_samples = 0;
		this->accumulator = 0;
		this->remove_offset = 0;
		outputstruct[0].HAlfaOutput = 0;
	}

	this->SignalsOutputInterface->Write();
	return True;
		
}
bool HAlphaGAM::ProcessHttpMessage(HttpStream &hStream){
	
	HtmlStream hmStream(hStream);
	int i;
	hmStream.SSPrintf(HtmlTagStreamMode, "html>\n\
		<head>\n\
		<title>%s</title>\n\
		</head>\n\
		<body>\n\
		<svg width=\"100&#37;\" height=\"100\" style=\"background-color: AliceBlue;\">\n\
		<image x=\"%d\" y=\"%d\" width=\"%d\" height=\"%d\" xlink:href=\"%s\" />\n\
		</svg", (char *) this->Name() ,0, 0, 422, 87, "http://www.ipfn.ist.utl.pt/ipfnPortalLayout/themes/ipfn/_img_/logoIPFN_Topo_officialColours.png");

	hmStream.SSPrintf(HtmlTagStreamMode, "br><br><text style=\"font-family:Arial;font-size:46\">%s</text><br", (char *) this->Name());

    FString submit_view;
    submit_view.SetSize(0);
    if (hStream.Switch("InputCommands.submit_view")){
        hStream.Seek(0);
        hStream.GetToken(submit_view, "");
        hStream.Switch((uint32)0);
    }
	if(submit_view.Size() > 0) view_input_variables = True;
	
	FString submit_hide;
    submit_hide.SetSize(0);
    if (hStream.Switch("InputCommands.submit_hide")){
        hStream.Seek(0);
        hStream.GetToken(submit_hide, "");
        hStream.Switch((uint32)0);
    }
	if(submit_hide.Size() > 0) view_input_variables = False;

	hmStream.SSPrintf(HtmlTagStreamMode, "form enctype=\"multipart/form-data\" method=\"post\"");
	if(!view_input_variables){
		hmStream.SSPrintf(HtmlTagStreamMode, "input type=\"submit\" name=\"submit_view\" value=\"View input variables\"");
	}
	else {
		hmStream.SSPrintf(HtmlTagStreamMode, "input type=\"submit\" name=\"submit_hide\" value=\"Hide input variables\"");		
	}
	hmStream.SSPrintf(HtmlTagStreamMode, "/form");
	
	hmStream.SSPrintf(HtmlTagStreamMode, "/body>\n</html");
	hStream.SSPrintf("OutputHttpOtions.Content-Type","text/html;charset=utf-8");
	hStream.WriteReplyHeader(True);

	return True;		
}
