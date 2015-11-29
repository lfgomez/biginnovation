function startup()
    print('in startup')
    dofile('test.lua')
    end

print('init.lua ver 1.2')
wifi.setmode(wifi.STATION)
print('set mode=STATION (mode='..wifi.getmode()..')')
print('MAC: ',wifi.sta.getmac())
print('chip: ',node.chipid())
print('heap: ',node.heap())
-- wifi config start
wifi.sta.config("FIAP-INMETRICS","hacka@fiap")
-- wifi config end

tmr.alarm(0,10000,0,startup)
