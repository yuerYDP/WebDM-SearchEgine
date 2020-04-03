#include "BMPImage.h"
#include "basic.h"
#include <iostream>

using namespace std;

void test_cvt2gray(){
    BMPImage src("./No.bmp");
    BMPImage dst = cvt2gray(src);
    dst.save("./gray.bmp");
}

int main(){
    test_cvt2gray();
    cout << "Test finishes." << endl;
    return 0;
}
