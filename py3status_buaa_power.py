import requests


class Py3status:
    format = 'BUAAPower: {power}'
    # Change your student id here or in py3status config file.
    user_id = '11111111'
    refresh_sec = 3600

    def new_north_ele(self):
        data = {
            'stucode': self.user_id,
            'type': 1
        }
        try:
            res = requests.post(
                'http://weixin.lrgj.net.cn/ics/rest/wxdev/getlvalue', json=data)
            res = res.json()['data']['provalue']
            remaining = float(res.replace('kWh', ''))
        except:
            return {
                'full_text': self.py3.safe_format(self.format, {'power': 'NaN'}),
                'cached_until': self.py3.time_in(10),
                'color': '#FF0000'
            }
        if remaining < 20:
            color = '#FF0000'
        else:
            color = '#FFFFFF'
        full_text = self.py3.safe_format(self.format, {'power': res})
        return {
            'full_text': full_text,
            'cached_until': self.py3.time_in(self.refresh_sec),
            'color': color
        }

    def on_click(self, event):
        pass
