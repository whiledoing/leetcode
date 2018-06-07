#include <iostream>
#include <string>
using namespace std;

template<typename T>
class SharedPtr {
public:
    SharedPtr(): m_data(NULL), m_cnt(NULL) {}

    SharedPtr(T* v) {
        m_data = v;
        m_cnt = new size_t(1);
    }

    ~SharedPtr() {
        if(m_cnt && --*m_cnt == 0) {
            delete m_data;
            delete m_cnt;
            cout << "desc" << endl;
        }
        m_data = NULL, m_cnt = NULL;
    }

    SharedPtr(const SharedPtr<T>& p) {
        m_data = p.m_data;
        m_cnt = p.m_cnt;
        ++*m_cnt;
    }

    SharedPtr<T>& operator= (const SharedPtr<T>& p) {
        if(m_cnt && --*m_cnt == 0) {
            delete m_data;
            delete m_cnt;
            cout << "desc" << endl;
        }

        m_data = p.m_data;
        m_cnt = p.m_cnt;
        ++*m_cnt;
        return *this;
    }

    friend ostream& operator << (ostream& os, const SharedPtr<T>& v) {
        os << "value is " << *v.m_data << ", cnt is " << *v.m_cnt;
        return os;
    }

    T& operator*() {
        return *m_data;
    }

    SharedPtr<T> clone() const {
        return *this;
    }

protected:
    T* m_data;
    size_t* m_cnt;
};

template<typename T>
SharedPtr<T> make_shared(const T& v) {
    return SharedPtr<T>(new T(v));
}

int main(int argc, char const *argv[])
{
    auto p1 = make_shared(3);
    auto p2 = p1;
    cout << *p1 << endl;
    *p1 = 444;
    cout << *p1 << endl;
    cout << p1 << endl;
    auto p3 = p1.clone();
    cout << p3 << endl;
    p1 = make_shared(4);
    cout << p1 << endl;
    return 0;
}
