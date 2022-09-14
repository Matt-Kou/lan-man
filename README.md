# lan-man
 A LAN management API

## Potential goals

### Easy registration of computers across OSes

Ideally, it would be like:
```python
import lanman
devices = lanman.list_unregistered()
for device in devices:
    device.register()
```
The user would not need to care about the OS or connectivity (ethernet or WiFi).

### Easy access of data

```python
# suppose there there two devices: d1, d2
with d1.use_camera(0) as d1_camera:
    d2.install(d1_camera)
```
Now d2 can use the camera 0 on d1 as if the camera is connected to itself. This can be used for video analysis. For example:
```python
# suppose there is a video analysis model that outputs the location of people
model.evaluate()
print(cameras.rooms()[model(torch.tensor(cameras.snapshot()))])
```
`cameras.snapshot()` here would output a snapshot of each camera and `cameras.rooms()` would output the rooms of the given index. This could be improved so that the movement and arrival/leave of each person can be recorded.

### Customized transmission of data

This could be a hard goal to achieve. The fundamental idea is: Using the current WiFi 6e, it is possible to achieve bit rate of 1200Mbps via a 160MHz channel. The bit rate of 1080p video at 60fps is around 4,500 to 9,000 Kbps. For 4K @ 60fps HEVC, the bit rate if around 48 to 54 Mbps. As a result, WiFi should be sufficient to be used for video transmission replacing HDMI (in some senarios). However, TCP is of course not an option for such purpose because the necessity of package verification is very low. Moreover, even packet switch could be abandoned. Circuit switching might be a better option for this usage.  


## Relavent Projects

1. [Home Assistant](https://www.home-assistant.io/)