#include <iostream>
#include <vector>
#include <string>
#include <numeric>
#include <algorithm>
using namespace std;

template<typename T>
class Heap {
private:
    vector<T> m_data;
public:
    Heap() {}

    Heap(const vector<T>& cp): Heap() {
        m_data.push_back(numeric_limits<T>::min());
        for(auto v : cp) insert(v);
    }

    void heapify() {
        for(int i = m_data.size()/2; i; --i) {
            this->shift_down(i);
        }
    }

    void shift_down(int start, int end=-1) {
        if(end == -1) end = m_data.size();
        for(int i = start, c = start; (c=2*i) < end; i=c) {
            if(c+1 < end && m_data[c+1] < m_data[c]) ++c;
            if(m_data[i] <= m_data[c]) return;
            swap(m_data[i], m_data[c]);
        }
    }

    T extract_min() {
        swap(m_data[1], m_data[m_data.size()-1]);
        T t = m_data[m_data.size()-1];
        m_data.pop_back();
        shift_down(1);
        return t;
    }

    void sort_data(bool reverse=true) {
        for(int i = m_data.size()-1; i; --i) {
            swap(m_data[1], m_data[i]);
            shift_down(1, i);
        }

        if(reverse) {
            std::reverse(m_data.begin()+1, m_data.end());
        }
    }

    void print() const {
        for(int i = 1; i < m_data.size(); ++i) {
            cout << m_data[i] << ' ';
        }
        cout << endl;
    }

    void shift_up(int start = -1) {
        if(start == -1) {
            start = m_data.size() - 1;
        }

        for(int i = start, p=start; m_data[p=i/2] > m_data[i]; i=p) {
            swap(m_data[i], m_data[p]);
        }
    }

    void insert(const T& v) {
        m_data.push_back(v);
        shift_up();
    }

    Heap<T> n_largest(int n) const {
        Heap<T> res;

        int i = 1;
        for(; i <= min(n, int(m_data.size()-1)); ++i) {
            res.insert(m_data[i]);
        }

        for(; i <= m_data.size()-1; ++i) {
            if(m_data[i] > res.m_data[1]) {
                res.replace_top(m_data[i]);
            }
        }

        res.sort_data(false);
        return res;
    }

    void replace_top(const T& v) {
        m_data[1] = v;
        shift_down(1);
    }
};

int main(int argc, char const *argv[])
{
    vector<int> test = {1, 2, 3, 5, 0, 2, 7, -1};
    Heap<int> h1(test);
    h1.print();
    h1.insert(-3);
    h1.print();

    h1.n_largest(5).print();
    // h1.sort_data();
    // h1.print();
    return 0;
}
