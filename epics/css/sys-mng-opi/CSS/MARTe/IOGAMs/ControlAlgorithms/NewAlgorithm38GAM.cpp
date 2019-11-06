#include "NewAlgorithm38GAM.h"

OBJECTLOADREGISTER(NewAlgorithm38GAM, "$Id: $")

//  ******** Default constructor ***********************************
NewAlgorithm38GAM::NewAlgorithm38GAM(){
	this->SignalsInputInterface = NULL;
	this->SignalsOutputInterface = NULL;
}

// ********* Destructor ********************************************
NewAlgorithm38GAM::~NewAlgorithm38GAM()
{
	if(this->SignalsInputInterface != NULL) delete[] this->SignalsInputInterface ;
	if(this->SignalsOutputInterface != NULL) delete[] this->SignalsOutputInterface;
}

//{ ********* Initialise the module ********************************
bool NewAlgorithm38GAM::Initialise(ConfigurationDataBase& cdbData){
	CDBExtended cdb(cdbData);
	return True;
}

//{ ********* Execute the module functionalities *******************
bool NewAlgorithm38GAM::Execute(GAM_FunctionNumbers functionNumber){
	InputInterfaceStruct *inputstruct = (InputInterfaceStruct *) this->SignalsInputInterface->Buffer();
	this->SignalsInputInterface->Read();
	OutputInterfaceStruct *outputstruct = (OutputInterfaceStruct *) this->SignalsOutputInterface->Buffer();
	this->SignalsOutputInterface->Write();
	return True;
}

bool NewAlgorithm38GAM::ProcessHttpMessage(HttpStream &hStream){
HtmlStream hmStream(hStream);
int i;
hmStream.SSPrintf(HtmlTagStreamMode, "html>\n\
	<head>\n\
	<title>%s</title>\n\
	</head>\n\
	<body>\n\
	<svg width="100&#37;" height="100" style="background-color: AliceBlue;">\n\
	<image x="%d" y="%d" width="%d" height="%d" xlink:href="%s" />\n\
	</svg", (char *) this->Name() ,0, 0, 422, 87, "http://www.ipfn.ist.utl.pt/ipfnPortalLayout/themes/ipfn/_img_/logoIPFN_Topo_officialColours.png");
hmStream.SSPrintf(HtmlTagStreamMode, "br><br><text style="font-family:Arial;font-size:46">%s</text><br", (char *) this->Name());
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
hmStream.SSPrintf(HtmlTagStreamMode, "form enctype="multipart/form-data" method="post"");
if(!view_input_variables){
	hmStream.SSPrintf(HtmlTagStreamMode, "input type="submit" name="submit_view" value="View input variables"");
}
hmStream.SSPrintf(HtmlTagStreamMode, "/form");
hmStream.SSPrintf(HtmlTagStreamMode, "/body>\n</html");
hStream.SSPrintf("OutputHttpOtions.Content-Type","text/html;charset=utf-8");
hStream.WriteReplyHeader(True);
return True;
}
