// Map.h
#ifndef MAP_H
#define MAP_H

#include <vector>

typedef unsigned int uint4;

using namespace std;

template <typename T> class Map {
    public:
	vector<int> dimsVec;
	uint4 rows;
	uint4 cols;
	uint4 channels;
	int dataType;
	T* data;

        /** @brief Default constructor
	 */
        Map():dimsVec({0, 0}), rows(0), cols(0), channels(1), dataType(1), data(nullptr);

        /** @brief Constructor
	  * @param _dimsVec, data dimisions
	  * @param _dataType, data type
	  * @param _data, data ptr
	 */
        Map(vector<int> &_dimsVec, int &_dataType, const T* &_data);

        /** @brief Constructor
	  * @param _dimsVec, data dimisions 
	  * @param _dataType, data type
	  * @param _init, using this value to initialize data
	 */
        Map(vector<int> &_dimsVec, int &_dataType, const T &_init=0);

        /** @brief Copy constructor
	  * @param rhs, the source
	 */
	Map(const Map<T>& rhs); // right hand side

        /** @brief Move constructor
	  * @param rhs, the source
	 */
	Map(Map<T>&& rhs);

        /** @brief Destructor
	 */
	~Map();

        /** @brief Assignment constructor
	  * @param rhs, data dimisions
	 */
	Map<T>& operator=(const Map<T>& rhs);

        /** @brief Move assignment constructor
	  * @param rhs, data dimisions
	 */
	Map<T>& operator=(Map<T>&& rhs);

        /** @brief Copy constructor
	  * @param rhs, data dimisions 
	 */
	Map<T>& operator[]();

        /** @brief Copy constructor
	  * @param rhs, data dimisions 
	 */
        Map reshape();

        /** @brief Copy constructor
	  * @param rhs, data dimisions 
	 */
	Map clone();

        /** @brief Copy constructor
	  * @param rhs, data dimisions 
	 */
	void create();
	
	Map<T> roi(Rect rect);
}
#endif // MAP_H
