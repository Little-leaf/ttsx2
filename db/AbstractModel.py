from django.db import models


def get_time():
    import time
    timeArray = time.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")
    tm_hour = timeArray.tm_hour
    tm_min = timeArray.tm_min
    tm_sec = timeArray.tm_sec
    if timeArray.tm_hour < 10:
        tm_hour = "0" + str(timeArray.tm_hour)
    if timeArray.tm_min < 10:
        tm_min = "0" + str(timeArray.tm_min)
    if timeArray.tm_sec < 10:
        tm_sec = "0" + str(timeArray.tm_sec)

        otherStyleTime = "%d年%d月%d日 %s:%s:%s" % (
            timeArray.tm_year, timeArray.tm_mon, timeArray.tm_mday, tm_hour, tm_min, tm_sec)
        return otherStyleTime


class AbstractModel(models.Model):
    """基类"""
    # 创建时间
    create_time = models.CharField(default=get_time, max_length=50, null=True)
    # 修改时间
    set_time = models.DateTimeField(auto_now=True)
    # 是否删除
    is_delete = models.BooleanField(default=False)

    # 抽象类
    class Meta:
        abstract = True


