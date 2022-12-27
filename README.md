# macro_SRT

Korea trail SRT macro file using Python script
It requires selenium, chrome web driver, and etc.

If you want to run the macro, you have to edit three lines of SRT_macro.py

driver = webdriver.Chrome("directory of chromedriver", chrome_options=options)

i.e.) home/Download/chromedriver

driver.find_element_by_id('srchDvNm01').send_keys("ID Number")
driver.find_element_by_id('hmpgPwdCphd01').send_keys("Password")

i.e.) SRT ID numeer and Passward

and, just run SRT_macro.py
!
python3 SRT_macro.py
!


referenced by https://net-gate.tistory.com/94
