#!/usr/bin/env python
#encoding: utf-8

# 【第一题】JSON格式转换
# 在某个特定应用场景中，我们有一个从JSON获取的内容，比如：
# m = { "a": 1, "b": { "c": 2, "d": [3,4] } }
# 现在需要把这个层级的结构做展开，只保留一层key/value结构。对于上述输入，需要得到的结构是：
# o = {"a": 1, "b.c": 2, "b.d": [3,4] }
# 也就是说，原来需要通过 m["b"]["c"] 访问的值，在展开后可以通过 o["b.c"] 访问。
# 请实现这个“层级结构展开”的代码。
# 输入：任意JSON（或者map/dict）
# 输出：展开后的JSON（或者map/dict）
def prob_1_with_map(data):
    # recursive loop for dict, put result in res
    res = {}
    def dfs(d, prefix=""):
        if prefix: prefix += '.'
        for k, v in d.items():
            if isinstance(v, dict):
                dfs(v, prefix+k)
            else:
                res[prefix+k] = v
    dfs(data)
    return res

def prob_1_with_json(data):
    import json
    return json.dumps(prob_1_with_map(json.loads(data)))

# 【第二题】数据存取
# 我们的程序运行过程中用到了一个数组a，数组元素是一个map/dict。
# 数组元素的“键”和“值”都是字符串类型。在不同的语言中，对应的类型是：
# PHP的array, Java的HashMap, C++的std::map, Objective-C的NSDictionary, Swift的Dictionary, Python的dict, JavaScript的object, 等等
# 示例：
# a[0]["key1"]="value1"
# a[0]["key2"]="value2"
# a[1]["keyA"]="valueA"
# ...
# 为了方便保存和加载，我们使用了一个基于文本的存储结构，数组元素每行一个：
# text="key1=value1;key2=value2\nkeyA=valueA\n..."
#
# 要求：请实现一个“保存”函数、一个“加载”函数。
# text=store(a);  //把数组保存到一个文本字符串中
# a=load(text); //把文本字符串中的内容读取为数组
# 必须严格按照上述的“每行一个、key=value”的格式保存。
class InvalidTextException(Exception):
    pass

def prob_2_store(a):
    return '\n'.join([';'.join(['%s=%s' % (k, v) for k, v in dict_item.items()]) for dict_item in a])

def prob_2_load(text):
    a = []
    for line in text.split('\n'):
        dict_item = {}
        for item in line.split(';'):
            try:
                equ_idx = item.index('=')
            except ValueError as e:
                raise InvalidTextException(e.message)
            dict_item[item[:equ_idx]] = item[equ_idx+1:]
        a.append(dict_item)
    return a

    # or maybe one-line code, but not good for error processing and readability
    # return [{item[:item.index('=')]:item[item.index('=')+1:] for item in line.split(';')} for line in text.split('\n')]

# 【第三题】路径规划
# 假设现在有一个有向无环图，每个节点上都带有正数权重。我们希望找到一条最优路径，使得这个路径上经过的节点的权重之和最大。
# 输入：n个节点，m个路径，起点
# 输出：最优路径的权重值之和
# 举例：
# 3个节点：
# A 1
# B 2
# C 2
# 3条路径：
# A->B
# B->C
# A->C
# 起点：
# A
# 输出：5  （最优路径是 A->B->C ， 权重之和是 1+2+2=5）
# 附加问题：我们要求的输入是有向无环图，但是没人知道实际使用的时候会有什么数据输入进来，如何避免输入了带环路的图导致的死循环呢？

def prob_3(node_value_list, path_list, start_node):
    # edge-list graph
    graph = {}
    for b, e in path_list:
        graph.setdefault(b, []).append(e)

    # dfs with circle detection
    prob_3.max_v = -1
    def dfs(start_node, path, sum_v):
        if start_node not in graph: return

        for e in graph[start_node]:
            # meet circle
            if e in path: return
            sum_v += node_value_list[e]
            prob_3.max_v = max(sum_v, prob_3.max_v)
            path.append(e)
            dfs(e, path, sum_v)
            path.pop()
            sum_v -= node_value_list[e]

    dfs(start_node, [], node_value_list[start_node])
    return prob_3.max_v

# 【第四题】最小差值
# 输入一个整数数组a，和一个整数k，对于a中每一个元素，必须进行一次操作（加上k或者减去k），要求是数组中所有元素执行完操作后，整个数组最大和最小值之差最小。
# 输出这个差值。
# 例如
# 输入：数组a为：[1, 7, 3, 5]，k为3
# 输出：4

def prob_4(nums, k):
    """
    时间复杂度O(n)

    1）如果min_v+k-(max_v-k) >= (max_v-min_v)，就不交换，最好的数值就是max_v-min_v。换句话说，如果max数值减k和min加k，这两个的差值
    还不如max和min本身数值，那么不论如何交换，最小值都不如所有数据都+k或者-k来的好。
    2）中间数值看靠近那个阈值更远（和中点比较）就往那个方向靠近。
    """
    min_v, max_v = min(nums), max(nums)
    if min_v + k >= max_v: return max_v - min_v

    max_v, min_v = max_v-k, min_v+k
    mid_v = (max_v+min_v)/2.0

    for v in nums:
        if v >= mid_v:
            min_v = min(min_v, v-k)
        else:
            max_v = max(max_v, v+k)
    return max_v - min_v

def check_eq(a, b):
    try:
        assert(a == b)
    except:
        print('%s not eq with %s' % (a, b))

if __name__ == '__main__':
    check_eq(prob_1_with_map({'a': 1, 'b': { 'c': 2, 'd': [3,4]}}), {
        'a': 1,
        'b.c': 2,
        'b.d': [3, 4]
    })

    a = [{"key1":"value1", "key2": "value2"}, {"keyA": "valueA"}]
    check_eq(prob_2_load(prob_2_store(a)), a)

    check_eq(prob_3([1, 2, 2], [(0, 1), (1, 2), (0, 2)], 0), 5)
    check_eq(prob_4([1, 3, 7, 5], 3), 4)
    check_eq(prob_4([1, 2, 3, 4], 1), 1)
    check_eq(prob_4([1, 2, 3, 4], 2), 3)
    check_eq(prob_4([1, 2, 3, 4], 3), 3)