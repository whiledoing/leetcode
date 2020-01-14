/*
 * @lc app=leetcode.cn id=208 lang=cpp
 *
 * [208] 实现 Trie (前缀树)
 *
 * https://leetcode-cn.com/problems/implement-trie-prefix-tree/description/
 *
 * algorithms
 * Medium (63.29%)
 * Likes:    177
 * Dislikes: 0
 * Total Accepted:    20.3K
 * Total Submissions: 32K
 * Testcase Example:  '["Trie","insert","search","search","startsWith","insert","search"]\n' +
  '[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]'
 *
 * 实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。
 *
 * 示例:
 *
 * Trie trie = new Trie();
 *
 * trie.insert("apple");
 * trie.search("apple");   // 返回 true
 * trie.search("app");     // 返回 false
 * trie.startsWith("app"); // 返回 true
 * trie.insert("app");
 * trie.search("app");     // 返回 true
 *
 * 说明:
 *
 *
 * 你可以假设所有的输入都是由小写字母 a-z 构成的。
 * 保证所有输入均为非空字符串。
 *
 *
 */
#include <iostream>
#include <string>
#include <vector>
#include <memory>
using namespace std;

// @lc code=start
class Trie {
public:
    /** Initialize your data structure here. */
    Trie() {
        root = new TrieNode();
    }

    ~Trie() {
        delete root;
    }

    /** Inserts a word into the trie. */
    void insert(string word) {
        shared_ptr<TrieNode> p_node = make_shared<TrieNode>(root);
        for (auto c : word) {
            if (p_node->node[c-'a'] == nullptr) {
                p_node->node[c-'a'] = make_shared<TrieNode>();
            }
            p_node = p_node->node[c-'a'];
        }

        p_node->m_is_value = true;
    }

    /** Returns if the word is in the trie. */
    bool search(string word) {
        shared_ptr<TrieNode> p_node = make_shared<TrieNode>(root);
        for (auto c : word) {
            p_node = p_node->node[c-'a'];
            if (p_node == nullptr) break;
        }
        return p_node && p_node->m_is_value;
    }

    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        shared_ptr<TrieNode> p_node = make_shared<TrieNode>(root);
        for (auto c : prefix) {
            p_node = p_node->node[c-'a'];
            if (p_node == nullptr) break;
        }
        return p_node != nullptr;
    }

private:
    struct TrieNode {
        TrieNode() {

        }

        vector<shared_ptr<TrieNode>> node = vector<shared_ptr<TrieNode>>(26);
        bool m_is_value;

        ~TrieNode() {
            cout << "del" << endl;
        }
    };

    TrieNode *root;
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */
// @lc code=end
int main(int argc, char const *argv[])
{
    Trie* obj = new Trie();
    obj->insert("apple");
    cout << obj->search("apple") << endl;
    delete obj;
    return 0;
}


