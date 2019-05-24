import asyncio
from pyppeteer import launch
import pyautogui
import time

width, height = 1366, 768
async def main():
    browser = await launch(headless=False, userDataDir='./userdata', args=['--disable-infobars',f'--window-size={width},{height}'])
    #browser = await launch(userDataDir='./userdata', args=['--disable-infobars',f'--window-size={width},{height}'])
    page = await browser.newPage()
    await page.setViewport({'width': width, 'height': height})
    #await page.goto('http://www.lxwc.com.cn')
    await page.goto('http://www.lxwc.com.cn/dailysign.php')
    try:
        await page.click("#JD_sign")
        print("签到成功！")
        await asyncio.sleep(5)
        await page.screenshot({'path': 'lxwcfinish.png', 'fullPage': True})
    except:
        print("已经签过到了！")
        await page.screenshot({'path': 'lxwcfinally.png', 'fullPage': True})

    await asyncio.sleep(10)

asyncio.get_event_loop().run_until_complete(main())