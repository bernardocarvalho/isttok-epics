//******************************************************************************
//    MARTe Library
//    $Log: driver_test.cpp,v $

//
//******************************************************************************

#include "HttpDigestRealm.h"
#include "System.h"
#include "FString.h"

int main(int argc, char **argv) {

	FString HA1;

	if (argc != 4){
		printf("Invalid number of args [%d]. Usage %s <userName> <password> <realm>\n", argc, argv[0]);
		return -1;
	}

	GeneratePasswordDigest(argv[1], argv[2], argv[3], HA1);

	printf("Generated hash for user = %s, password = %s, real = %s -> %s\n", argv[1], argv[2], argv[3], HA1.Buffer());

/*
	FString toEncode;
	toEncode = "oper";
	unsigned char buffer[16];

md5( (unsigned char *)toEncode.BufferReference(), toEncode.Size(),buffer);
for ( i=0;i<16;i++){  
    printf("%02x",buffer[i]);
}

	printf("\n");
	printf("Hash is %s\n", HA1.Buffer());


    HA1.SetSize(0);
    toEncode.Printf("%s:%s:%s","opertok","SECURITY.PASSWORD","oper");
    md5( (unsigned char *)toEncode.BufferReference(), toEncode.Size(),buffer);
    for (int i=0;i<16;i++){
        HA1.Printf("%02x",buffer[i]);
    }

*/

	return 0;
}
