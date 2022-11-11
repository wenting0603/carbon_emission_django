# carbon_emission_django

建立一個建議的計算機

## 1.前端網頁
mysite/test/template/*html

CSS設定+html

mysite/mysite/urls.py

註冊app的urls在網頁上呈現

## 2.獲取前端資料於後台計算

mysite/test/views.py

建立各項對應前端的function 

1.獲取現在時間並返回前端


2.獲取前端使用者輸入資訊進行計算後輸入DB

## 3.將計算資料存入django內建資料庫
mysite/test/models.py

建立DB的外殼，設定需要的欄位

mysite/test/admin.py

設定DB如何呈現

## 4.呈現
資料輸入頁面

<img width="788" alt="image" src="https://user-images.githubusercontent.com/64676970/201253817-db6f9eac-a1aa-47a6-bef3-69c91f81afab.png">

計算後回送

<img width="813" alt="image" src="https://user-images.githubusercontent.com/64676970/201253945-c575394f-0cd6-4ed2-93be-f15028a6f774.png">

資料庫

<img width="753" alt="image" src="https://user-images.githubusercontent.com/64676970/201254115-20136529-3025-4c18-a03b-e822df2f120c.png">

