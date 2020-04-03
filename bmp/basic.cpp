#include "basic.h"
#include "BMPImage.h"
#include "basic.h"
#include <cstddef>

typedef unsigned int uint;   // 4 bytes
typedef unsigned char uchar; // 1 byte

BMPImage cvt2gray(const BMPImage &src){
	BMPImage dst = src;
	uchar *m_data = dst.imgData();
	int4 m_width = dst.width();
	int4 m_height = dst.height();
	ulong m_row_size = dst.rowSize();
	uchar val;
	size_t pos;
	uchar *tmp_data = new uchar[dst.infoHeader().biSizeImage];
	for (uint i = 0; i < m_height; i++){
		for (uint j = 0; j < m_width; j++){
			pos = i * m_row_size + j * 3;
			val = 0.114 * m_data[pos] + 0.587 * m_data[pos + 1] + 0.299 * m_data[pos + 2]; // the order is b, g, r
			// 下面的两种方式是错误的，因为在原来的基础上改动的话，当 height >0 时，先修改下半幅图，接着 pos 就到了下半幅图，所以最后的结果是上下对称
//			dst.bgr(i, j) = BGR{val, val, val};
//			dst.bgr(i, j).b = val;
//			dst.bgr(i, j).g = val;
//			dst.bgr(i, j).r = val;
			tmp_data[pos] = val;
			tmp_data[pos + 1] = val;
			tmp_data[pos + 2] = val;
		}
	}

	dst.resetData(tmp_data);
	delete [] tmp_data;
	return dst;
}
