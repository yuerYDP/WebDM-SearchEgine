//Main.cpp
#include <iostream>
#include "BMPImage.h"

void testBMP(){
    // -----------创建一张24位纯黑的图像----------
    BMPImage bmp24_101;
    bmp24_101.create(101,101);
    bmp24_101.save("./24_101.bmp");
    BGR green = {0,255,0};
    // 将左上的50*20像素修改为绿色
    for(uint4 i = 0;i<50;i++){
        for(uint4 j = 0;j<20;j++){
            bmp24_101.bgr(i, j) = green;
        }
    }
    // 保存
    bmp24_101.save("./24_101_1.bmp");

    // -----------创建一张24位纯黑图像--------
    BMPImage bmp_24_500(500,500);
    // 将左上的50*20像素修改为绿色
    for(uint4 i = 0;i<50;i++){
        for(uint4 j = 0;j<20;j++){
            bmp_24_500.bgr(i, j) = green;
        }
    }
    //保存
    bmp_24_500.save("./24_500.bmp");

    // -----------创建一张32位的纯黑图像------
    BMPImage bmp_32(233,233,32);
    BGRA red{0,0,255,255};
    // 将左上的50*20像素修改为红色
    for(uint4 i = 0;i<50;i++){
        for(uint4 j = 0;j<20;j++){
            bmp_32.bgra(i, j) = red;
        }
    }
    bmp_32.save("./32.bmp");

    // ----------打开一张位图--------------
    BMPImage bmpImage1("./No.bmp");
    // 将一块区域修改为绿色
    for(uint4 i = 100;i<200;i++){
        for(uint4 j = 100;j<200;j++){
            bmpImage1.bgr(i, j) = green;
        }
    }
    // 保存
    bmpImage1.save("./2.bmp");

    // ----------打开一张32位图--------------
    BMPImage bmp_o_32("./32.bmp");
    // 将一块区域修改为蓝色
    BGRA blue{255,0,0,255};
    for(uint4 i = 100;i<200;i++){
        for(uint4 j = 100;j<200;j++){
            bmp_o_32.bgra(i, j) = blue;
        }
    }
    // 保存
    bmp_o_32.save("./32_1.bmp");
}

int main() {
    testBMP();
    std::cout << "Hello, World!" << std::endl;
    //getchar();
    return 0;
}
