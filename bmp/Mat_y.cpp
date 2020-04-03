#include "Map.h"

template <typename T>
Map :: Map(vector<int> &_dimsVec, int &_dataType, const T* &_data)
{
    rows = _dimsVec[1h
}

template <typename T>
Map(vector<int> &_dimsVec, int &_dataType, const T &_init);

template <typename T>
Map(const Map<T>& rhs); // right hand side

template <typename T>
Map(const Map<T>&& rhs);

~Map();

template <typename T>
Map<T>& operator=(const Map<T>& rhs)
{
    if (this = &rhs)
    {
        return *this;
    }
}

Map<T>& operator=(const Map<T>&& rhs);

Map<T>& operator[](const Map<T>& rhs);

Map reshape();

Map clone();

void create();
#endif // MAP_H
