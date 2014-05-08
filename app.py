from flask import Flask, render_template, url_for
app = Flask(__name__)
import json
import time
import urllib

@app.route('/')
def hello_world():
    return render_template('index.html',dataSource="/username.json")

@app.route("/username.json")
def testData():
    return '{"1367737200":0,"1367823600":0,"1367910000":0,"1367996400":0,"1368082800":0,"1368169200":0,"1368255600":0,"1368342000":1,"1368428400":1,"1368514800":1,"1368601200":1,"1368687600":1,"1368774000":1,"1368860400":0,"1368946800":0,"1369033200":0,"1369119600":0,"1369206000":0,"1369292400":0,"1369378800":0,"1369465200":1,"1369551600":0,"1369638000":0,"1369724400":0,"1369810800":0,"1369897200":0,"1369983600":0,"1370070000":1,"1370156400":0,"1370242800":0,"1370329200":0,"1370415600":0,"1370502000":0,"1370588400":0,"1370674800":1,"1370761200":1,"1370847600":1,"1370934000":1,"1371020400":1,"1371106800":1,"1371193200":1,"1371279600":0,"1371366000":0,"1371452400":0,"1371538800":0,"1371625200":0,"1371711600":0,"1371798000":0,"1371884400":0,"1371970800":4,"1372057200":4,"1372143600":4,"1372230000":4,"1372316400":0,"1372402800":0,"1372489200":4,"1372575600":4,"1372662000":0,"1372748400":0,"1372834800":4,"1372921200":0,"1373007600":0,"1373094000":4,"1373180400":4,"1373266800":0,"1373353200":0,"1373439600":4,"1373526000":0,"1373612400":0,"1373698800":4,"1373785200":4,"1373871600":0,"1373958000":0,"1374044400":4,"1374130800":4,"1374217200":4,"1374303600":4,"1374390000":0,"1374476400":0,"1374562800":0,"1374649200":0,"1374735600":0,"1374822000":0,"1374908400":0,"1374994800":8,"1375081200":8,"1375167600":8,"1375254000":8,"1375340400":8,"1375426800":8,"1375513200":8,"1375599600":8,"1375686000":0,"1375772400":0,"1375858800":8,"1375945200":0,"1376031600":0,"1376118000":8,"1376204400":8,"1376290800":0,"1376377200":0,"1376463600":8,"1376550000":0,"1376636400":0,"1376722800":8,"1376809200":8,"1376895600":0,"1376982000":0,"1377068400":0,"1377154800":0,"1377241200":0,"1377327600":8,"1377414000":0,"1377500400":0,"1377586800":0,"1377673200":0,"1377759600":0,"1377846000":0,"1377932400":0,"1378018800":14,"1378105200":14,"1378191600":14,"1378278000":14,"1378364400":14,"1378450800":14,"1378537200":14,"1378623600":14,"1378710000":0,"1378796400":0,"1378882800":14,"1378969200":0,"1379055600":0,"1379142000":0,"1379228400":14,"1379314800":0,"1379401200":0,"1379487600":14,"1379574000":14,"1379660400":0,"1379746800":0,"1379833200":14,"1379919600":0,"1380006000":0,"1380092400":14,"1380178800":0,"1380265200":14,"1380351600":0,"1380438000":0,"1380524400":14,"1380610800":14,"1380697200":0,"1380783600":0,"1380870000":0,"1380956400":14,"1381042800":0,"1381129200":0,"1381215600":0,"1381302000":0,"1381388400":0,"1381474800":0,"1381561200":0,"1381647600":1,"1381734000":1,"1381820400":1,"1381906800":1,"1381993200":1,"1382079600":1,"1382166000":1,"1382252400":0,"1382338800":0,"1382425200":1,"1382511600":0,"1382598000":0,"1382684400":0,"1382770800":0,"1382857200":0,"1382943600":0,"1383030000":0,"1383116400":1,"1383202800":0,"1383289200":0,"1383375600":0,"1383462000":0,"1383552000":0,"1383638400":0,"1383724800":0,"1383811200":1,"1383897600":0,"1383984000":0,"1384070400":1,"1384156800":1,"1384243200":1,"1384329600":1,"1384416000":1,"1384502400":1,"1384588800":1,"1384675200":0,"1384761600":0,"1384848000":0,"1384934400":0,"1385020800":0,"1385107200":0,"1385193600":0,"1385280000":0,"1385366400":4,"1385452800":4,"1385539200":4,"1385625600":4,"1385712000":4,"1385798400":4,"1385884800":4,"1385971200":0,"1386057600":0,"1386144000":4,"1386230400":0,"1386316800":0,"1386403200":0,"1386489600":4,"1386576000":0,"1386662400":0,"1386748800":4,"1386835200":0,"1386921600":0,"1387008000":0,"1387094400":0,"1387180800":4,"1387267200":4,"1387353600":4,"1387440000":4,"1387526400":4,"1387612800":4,"1387699200":0,"1387785600":0,"1387872000":0,"1387958400":0,"1388044800":0,"1388131200":0,"1388217600":0,"1388304000":8,"1388390400":8,"1388476800":8,"1388563200":8,"1388649600":8,"1388736000":8,"1388822400":8,"1388908800":0,"1388995200":8,"1389081600":0,"1389168000":0,"1389254400":0,"1389340800":0,"1389427200":0,"1389513600":0,"1389600000":0,"1389686400":8,"1389772800":0,"1389859200":0,"1389945600":0,"1390032000":0,"1390118400":0,"1390204800":8,"1390291200":0,"1390377600":0,"1390464000":0,"1390550400":0,"1390636800":0,"1390723200":8,"1390809600":8,"1390896000":8,"1390982400":8,"1391068800":8,"1391155200":8,"1391241600":8,"1391328000":0,"1391414400":0,"1391500800":0,"1391587200":0,"1391673600":0,"1391760000":0,"1391846400":0,"1391932800":14,"1392019200":14,"1392105600":14,"1392192000":14,"1392278400":14,"1392364800":14,"1392451200":14,"1392537600":14,"1392624000":0,"1392710400":0,"1392796800":14,"1392883200":0,"1392969600":0,"1393056000":14,"1393142400":14,"1393228800":0,"1393315200":0,"1393401600":14,"1393488000":0,"1393574400":0,"1393660800":14,"1393747200":14,"1393833600":0,"1393920000":0,"1394006400":0,"1394092800":0,"1394179200":0,"1394265600":14,"1394352000":0,"1394434800":0,"1394521200":0,"1394607600":0,"1394694000":0,"1394780400":0,"1394866800":0,"1394953200":0,"1395039600":1,"1395126000":0,"1395212400":0,"1395298800":0,"1395385200":0,"1395471600":0,"1395558000":1,"1395644400":0,"1395730800":0,"1395817200":0,"1395903600":0,"1395990000":0,"1396076400":0,"1396162800":1,"1396249200":0,"1396335600":0,"1396422000":0,"1396508400":1,"1396594800":0,"1396681200":1,"1396767600":1,"1396854000":0,"1396940400":0,"1397026800":1,"1397113200":0,"1397199600":0,"1397286000":0,"1397372400":0,"1397458800":1,"1397545200":1,"1397631600":0,"1397718000":0,"1397804400":0,"1397890800":0,"1397977200":0,"1398063600":0,"1398150000":0,"1398236400":0,"1398322800":0,"1398409200":0,"1398495600":0,"1398582000":0,"1398668400":0,"1398754800":0,"1398841200":0,"1398927600":0,"1399014000":0,"1399100400":0}'

@app.route('/<username>/calender')
def userCalander(username):
    return render_template('index.html',dataSource=url_for('data',username=username))


@app.route('/<username>/data.json')
def data(username):
    data = urllib.urlopen('https://github.com/users/%s/contributions_calendar_data' % username).read()

    data = json.loads(data)

    timeobj = {}

    for item in data:
        timeStamp = time.strptime(item[0],'%Y/%m/%d')
        timeStamp = time.mktime(timeStamp)
        timeobj[timeStamp] = item[1]

    return json.dumps(timeobj)

if __name__ == '__main__':
    app.run(debug=True)