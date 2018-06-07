#include <iostream>
#include <string>
#include <vector>
#include <cstring>
#include <cstdlib>
#include <map>
#include <ctime>
#include <set>
#include <typeinfo>
using namespace std;

/* 链表实现 */
class ListSet
{
public:
    ListSet(int max_value, int max_size) : m_max_value(max_value),
        m_size(max_size) {
        all_nodes = new node[max_size + 1];
        head = sentinel = &all_nodes[0];
        head->val = max_value;
        head->next = NULL;
        n = 0;
    }

    ~ListSet() {
        delete[] all_nodes;
    }

    void insert(int t);
    int size() {
        return n;
    }
    void report(int* v);

private:
    int m_max_value;
    int m_size;

    struct node {
        int val;
        node* next;
        node() {}
        node(int v, node* p) : val(v), next(p) {}
    };

    int n;
    node* all_nodes;    // 预先分配了所有内存空间
    node* head;
    node* sentinel;
};

// 使用循环的方式加入一个节点
void ListSet::insert(int t)
{
    /* 两种实现方式, 第一种, 保存pre和p的方式, 进行链表的插入 */

    /* 第一种
    node* p = head;
    node* pre = NULL;
    while(p->val < t) {
        pre = p;
        p = p->next;
    }

    if(p->val > t) {
        node* new_node = &all_nodes[++n];   // 从内存池中得到一个新的节点
        new_node->val = t;
        new_node->next = p;
        if(pre == NULL)
            head = new_node;
        else
            pre->next = new_node;
    }
    */

    /* 第二种, 使用直接改变前一个指针next指针的内容 */
    node** p = &head;
    /* 找到第一个不小于的节点 */
    for(; (*p)->val < t; p = &((*p)->next));

    /* 如果当前节点大, 那么在这个节点之前插入一个节点, 明确*p就是直接对应了pre的next对应地址中的内容, 直接修改 */
    if((*p)->val > t) {
        node* new_node = &all_nodes[++n];
        new_node->val = t;
        new_node->next = *p;
        *p = new_node;

        /* 如果不使用内存池的方式, 代码更加简单 */
        /* *p = node(t, *p); */
    }
}

void ListSet::report(int* v)
{
    int j = -1;
    for(node* p = head; p != sentinel; p = p->next)
        v[++j] = p->val;
}

class BSTSet
{
public:
    BSTSet(int maxv, int maxs) : max_val(maxv), max_size(maxs), n(0), root(0) {}
    void insert(int t) {
        /* 第一种使用, reverse insert 的递归形式 */
        // root = rinsert(root, t);

        /* 第二种使用, 直接调用循环的方式, 这里就体现出使用指向指针的指针方法的好处, 不需要保存
        pre指针, 以及到底是走了左子树还是右子树, 甚至是如果root为空, 也可以直接的修改 */
        node** p = &root;
        while(*p) {
            if((*p)->val == t)  return;

            if(t < (*p)->val)
                p = &((*p)->left);
            else
                p = &((*p)->right);
        }

        *p = new node(t);
        ++n;
    }

    int size() const {
        return n;
    }

    void report(int* d) {
        output_p = d;
        output_count = -1;
        travse(root);
    }

private:
    struct node {
        node(int t, node* l = NULL, node* r = NULL) : val(t), left(l), right(r) {}
        int val;
        node* left;
        node* right;
    };

private:
    void travse(node* p) {
        if(p == NULL)   return;

        travse(p->left);
        output_p[++output_count] = p->val;
        travse(p->right);
    }

    node* rinsert(node* p, int t) {
        if(p == NULL) {
            p = new node(t);
            ++n;
        } else if(p->val > t) {
            p->left = rinsert(p->left, t);
        } else if(p->val < t) {
            p->right = rinsert(p->right, t);
        }

        return p;
    }

    int* output_p;
    int output_count;
    node* root;

    int n ;
    int max_val;
    int max_size;
};

class BitSet
{
public:
    BitSet(int maxv, int maxs) : max_val(maxv), max_size(maxs), n(0) {
        int size = 1 + (maxv >> SHIFT);
        x = new int32_t[size];
        memset(x, 0, sizeof(int32_t)*size);
    }

    enum { BITSPERWORD = 32, SHIFT = 5, MASK = 0x1f };
    void insert(int t) {
        if(test(t)) return;
        set(t);
        ++n;
    }

    void report(int* d) {
        int c = -1;
        for(int i = 0; i < max_val; ++i)
            if(test(i))
                d[++c] = i;
    }

    int size() const {
        return n;
    }

private:
    bool test(int i) {
        return x[i >> SHIFT] & (1u << (i & MASK));
    }

    void clr(int i) {
        x[i >> SHIFT] &= ~(1u << (i & MASK));
    }

    void set(int i) {
        x[i >> SHIFT] |= (1u << (i & MASK));
    }

private:
    int max_val, max_size;
    int* x;
    int n;
};

/* 使用2的整数秘表示bin的大小 */
#define USING_2_N_SIZE_NUM_PER_BIN
class BinSet
{
public:
    BinSet(int maxv, int maxs) : max_val(maxv), max_size(maxs), n(0) {
        bins = new node*[max_size];
        sentinel = new node(max_val, NULL);

        /* 所有链表的尾节点都是一个sentinel */
        for(int i = 0; i < max_size; ++i)
            bins[i] = sentinel;

        int less_num_per_bin = max_val / max_size;
#ifdef USING_2_N_SIZE_NUM_PER_BIN
        /* 转换为2^bin_shift >= less_num_per_bin的最小值 */
        for(bin_shift = 0; less_num_per_bin; less_num_per_bin >>= 1, ++bin_shift);
        num_per_bin = 1 << bin_shift;
#else
        num_per_bin = 1 + less_num_per_bin;
#endif
    }

    void insert(int t) {
#ifdef USING_2_N_SIZE_NUM_PER_BIN
        int index = t >> bin_shift;
#else
        int index = t / num_per_bin;
#endif
        bins[index] = rinsert(bins[index], t);
    }

    int size() const {
        return n;
    }

    void report(int* d) {
        int c = -1;
        for(int i = 0; i < max_size; ++i)
            for(node* p = bins[i]; p != sentinel; p = p->next)
                d[++c] = p->val;
    }

private:
    struct node {
        node(int v, node* p) : val(v), next(p) {}
        int val;
        node* next;
    };
    node** bins;
    node* sentinel;

    node* rinsert(node* p, int t) {
        if(t > p->val) {
            p->next = rinsert(p->next, t);
        } else if(t < p->val) {
            p = new node(t, p);
            ++n;
        }

        return p;
    }

#ifdef USING_2_N_SIZE_NUM_PER_BIN
    int bin_shift;
#endif
    int num_per_bin;
    int max_val, max_size;
    int n;
};

template<typename SetType>
void gen_n_m(int n, int m)
{
    cout << "calling type : " << typeid(SetType).name() << endl;
    SetType s(n, m);
    while(s.size() != m)
        s.insert(rand() % n);

    int* d = new int[m];
    s.report(d);

    for(int i = 0; i < m; ++i)
        cout << d[i] << " ";
    cout << endl;

    delete[] d;
}

/* 使用floyd算法取样 */
template<typename SetType>
void gen_n_m_using_floyd(int n, int m)
{
    cout << "calling floyd algorithm using type : "
         << typeid(SetType).name() << endl;

    SetType s(n, m);
    for(int i = n - m; i < n; ++i) {
        int t = rand() % (n - m + 1);
        int old_size = s.size();
        s.insert(t);
        if(old_size == s.size())
            s.insert(i);
    }

    int* d = new int[m];
    s.report(d);

    for(int i = 0; i < m; ++i)
        cout << d[i] << " ";
    cout << endl;

    delete[] d;
}

int main(int argc, char const* argv[])
{
    srand(time(NULL));
    cout << rand() << endl;
    return 0;

    {
        int n = 10, m = 2;

        gen_n_m<ListSet>(n, m);
        gen_n_m<BSTSet>(n, m);
        gen_n_m<BitSet>(n, m);
        gen_n_m<BinSet>(n, m);

        gen_n_m_using_floyd<ListSet>(n, m);
        gen_n_m_using_floyd<BSTSet>(n, m);
        gen_n_m_using_floyd<BitSet>(n, m);
        gen_n_m_using_floyd<BinSet>(n, m);
    }

    {
        int n = 100, m = 99;

        gen_n_m<ListSet>(n, m);
        gen_n_m<BSTSet>(n, m);
        gen_n_m<BitSet>(n, m);
        gen_n_m<BinSet>(n, m);

        gen_n_m_using_floyd<ListSet>(n, m);
        gen_n_m_using_floyd<BSTSet>(n, m);
        gen_n_m_using_floyd<BitSet>(n, m);
        gen_n_m_using_floyd<BinSet>(n, m);
    }
}