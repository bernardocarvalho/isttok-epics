#ifndef _NEWALGORITHM_H
#define	_NEWALGORITHM_H

#include "DDBInputInterface.h"
#include "DDBOutputInterface.h"
#include "GAM.h"
#include "File.h"
#include "Matrix.h"
#include "HtmlStream.h"

OBJECT_DLL(NewAlgorithmGAM)

class NewAlgorithmGAM : public GAM, public HttpInterface {
private:

	DDBInputInterface *SignalsInputInterface;
	DDBOutputInterface *SignalsOutputInterface;

	struct InputInterfaceStruct {
	};

	struct OutputInterfaceStruct {
	};

	bool view_input_variables;
	
public:

	// Default constructor
	NewAlgorithmGAM();

	// Destructor
	virtual ~NewAlgorithmGAM();

	// Initialise the module
	virtual bool Initialise(ConfigurationDataBase& cdbData);

	// Execute the module functionalities
	virtual bool Execute(GAM_FunctionNumbers functionNumber);

	virtual bool ProcessHttpMessage(HttpStream &hStream);

	OBJECT_DLL_STUFF(NewAlgorithmGAM)
};



#endif