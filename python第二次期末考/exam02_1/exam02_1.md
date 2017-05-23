# 三角形判斷 #

## 說明 ##

讓使用者依序輸入三個整數，代表三角形的三個邊長。<br>
請判斷：<br>
<ol>

1. 判斷是否能成三角形，若可以便輸出「True」;若不行便輸出「False」<b>並結束程式</b>。<br>

2. 判斷是否為直角三角形，若為直角三角形便輸出「Right Triangle」，否則輸出「Non-Right Triangle」。
</ol>
<br>
1. 三角形的判斷方法：「任兩邊長的和<b>大於</b>第三邊」<br>
2. 直角三角形的判斷方法：「兩短邊平方和 = 最長邊平方」(a^2 + b^2 = c^2)<br>
*^代表平方<br>
<br>
![](triangle.gif) <br>


## Input Format ##

整數<br>
整數<br>
整數<br>

## Output Format ##

True 或 False<br>
Right Triangle 或 Non-Right Triangle (如果上題是True才會顯示這段) <br>

## Sample Input 1 ##
```
6
8
10
```

## Sample Output 1 ##
```
True
Right Triangle
```

## Sample Input 2 ##
```
10
30
12
```

## Sample Output 2 ##
```
False
```
## Hint ##

```
1. 當第一題判斷為False時，就要結束程式。
2. 輸出最末端沒有任何空格。
3. 兩邊長的和等於第三邊時就不是三角形。

```
