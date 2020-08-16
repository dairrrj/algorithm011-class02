* 位运算　　


| 动作 | 运算符 |
| --- | --- |
| 左移 |<<  |
| 右移 | >>  |
| 按位或 |&#124; |
| 按位与 | & |
| 按位取反 | ~ |
| 按位异或 | ^ |

异或的高级操作　　

1.  x^0 = x   　　//和0异或不变
2.  x^1s(~0) = ~x　 //和1异或取反
3.  x^(~x) = 1s　  //和本身取反异或全为1
4.  x^x = 0 　//和本身异或全为0
5.  c = a^b => a^c=b,b^c=a 
6.  a^b^c = a^(b^c) = (a^b)^c　 交换律

指定位置的位运算  

1. 将x最右边的n位清零：x&(~0<<n)
2. 获取x的第n位值（0或者1）：(x>>n)&1
3. 获取x的第n位的幂值：x&(1<<n)
4. 仅将第n位置为1：x|(1<<n)
5. 仅将第n位置为0：x&(~(1<<n))
6. 将x最高位至第n位(含)清零：x&((1<<n)-1)
7. 判断奇偶：(x&1)==1 表示为奇数;(x&1)==0 表示为偶数
8. 右移一位等于十进制除以2
9. 清零最低位的1：x&(x-1)
10. d
11. 得到最低为的1：x&-x
12. x&~x==0


* 排序算法

选择排序
```
def selection_sort(a):
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            if a[min_idx] > a[j]:
                min_idx = j
        a[i],a[min_idx] = a[min_idx],a[i]
```
插入排序
```
def insertion_sort(a):
    n = len(a)
    for i in range(1,n):
        key = a[i]
        j = i-1
        while j>=0 and key < a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
```
冒泡排序
```
def bubble_sort(a):
    n = len(a)
    for i in range(n):
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
```
归并排序
快速排序
```
def quick_sort(a,low,high):
    if low < high:
        pi = partition(a,low,high)
        quick_sort(a, low,pi-1)
        quick_sort(a, pi+1, high)
    
def partition(a,low,high):
    i = (low-1)
    piviot = a[high]
    for j in range(low,high):
        if a[j] <= piviot:
            i += 1
            a[i], a[j] = a[j], a[i]

    a[i + 1], a[high] = a[high], a[i + 1]
    return (i + 1)
```

