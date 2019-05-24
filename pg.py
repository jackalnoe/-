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
    await page.goto('http://bbs.pinggu.org/plugin.php?id=dsu_paulsign:sign')
    try:
        await page.click("#ct>div.mn>div.zhenghe>div:nth-child(2)>div.luntanbi>table>tbody>tr:nth-child(8)>td>a")
        await page.click("#qiandao>table>tbody>tr:nth-child(3)>td.qdnewtd3>a")
        print("签到成功！")
        await asyncio.sleep(5)
        await page.screenshot({'path': 'pgfinish.png', 'fullPage': True})
    except:
        print("已经签过到了！")
        await page.screenshot({'path': 'pgfinally.png', 'fullPage': True})
    await asyncio.sleep(10)
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())