# 標準函式庫 (time) #

## 說明 ##

使用者輸入一數字<br>
(從1970年1/1上午8:00至今所經過的時間)<br>
並將其轉換成以下時間格式輸出<code>世界標準時間</code>與<code>台灣時間</code><br>
例如：<br>
2017-10-20 02:30:55 (yyyy-mm-dd HH:MM:SS)<br>
2017-10-20 10:30:55 (yyyy-mm-dd HH:MM:SS)<br>

## Input Format ##

浮點數or整數<br>

## Output Format ##

yyyy-mm-dd HH:MM:SS (格式化時間：yyyy(西元年)；mm(月份)；dd(日)；HH(時(24hr制))；MM(分)；SS(秒)

## Sample Input 1 ##
```
1490703583.6294702
```

## Sample Output ##
```
2017-03-28 12:19:43
2017-03-28 20:19:43
```

## Hint ##

```
1. 輸出格式中，「dd HH」之間有空格隔開。
2. 輸出最末端(SS後面)無任何空格
<code>
time.gmtime()
time.localtime()
time.strftime()
</code>

```
