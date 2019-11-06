#ifndef _NEWALGORITHM38_H_
#define	_NEWALGORITHM38_H_

#include "DDBInputInterface.h"
#include "DDBOutputInterface.h"
#include "GAM.h"
#include "File.h"
#include "Matrix.h"
#include "HtmlStream.h"

OBJECT_DLL(NewAlgorithm38GAM)
class NewAlgorithm38GAM : public GAM, public HttpInterface {
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
	NewAlgorithm38GAM();

	// Destructor
	virtual ~NewAlgorithm38GAM();

	// Initialise the module
	virtual bool Initialise(ConfigurationDataBase& cdbData);

	// Execute the module functionalities
	virtual bool Execute(GAM_FunctionNumbers functionNumber);
	virtual bool ProcessHttpMessage(HttpStream &hStream);

	OBJECT_DLL_STUFF(NewAlgorithm38GAM)
};

#endif
