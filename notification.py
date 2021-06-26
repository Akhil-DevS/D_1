from plyer import notification
title='important'
message='drink water regularly'
notification.notify(title=title,
                    message=message,
                    app_icon=None,
                    timeout=10,
                    ticker='drink water',
                    toast="drink water")