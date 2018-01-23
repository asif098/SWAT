precinfofile = open(r'D:\Research\SWAT\Ganges\Stations\prec_station.txt','r')
precinfo = precinfofile.readlines()
prec = []
lat = []
lon = []
elevation = []
for i in range(1, len(precinfo)):
    line = precinfo[i].split(',')
    prec.append(line[1][1:])
    lat.append(line[2])
    lon.append(line[3])
    elevation.append(line[4][:-1])
    
solarfile = open(r'D:\Research\SWAT\SWAT_wgn\Source_files\Solar_radiation.csv','r')
solarinfo = solarfile.readlines()
slat = []
slon = []
solar = []
for i in range(1, len(solarinfo)):
    sline = solarinfo[i].split(',')
    slat.append(sline[0])
    slon.append(sline[1])
    s = ""
    for j in xrange(12):
        s = s + "," + sline[j+2]
    solar.append(s)

dewpfile = open(r'D:\Research\SWAT\SWAT_wgn\Source_files\dewp_monthly_avg.txt','r')
dewpinfo = dewpfile.readlines()
st_name=[]
dewp = []
for i in range(1, len(dewpinfo)):
    dline = dewpinfo[i].split(',')
    st_name.append(dline[0])
    d = ""
    for j in xrange(12):
        d = d + "," + dline[j+1]
    dewp.append(d)


windfile = open(r'D:\Research\SWAT\SWAT_wgn\Source_files\wind_monthly_avg.txt','r')
windinfo = windfile.readlines()
wind = []
for i in range(1, len(windinfo)):
    wline = windinfo[i].split(',')
    w = ""
    for j in xrange(12):
        w = w + "," + wline[j+1]
    wind.append(w)

    
fname = open(r'D:\Research\SWAT\SWAT_wgn\Ganges\wgninput.txt', 'a')

for i in range(0,len(prec)):
    filename = open(r"C:\Users\asif098\Google Drive\Laptop_dell\Research\SWAT\Input_DATA\SWAT_data\input_weather\MODWEC_input\\"+ prec[i] + '.WP1', 'r')
    inputdata = filename.readlines()
    line = prec[i]+ "," + lat[i] +"," + lon[i] + ","+elevation[i]+',' + "10"
    rainhh = []
    for j in range(2, 12):
        if j==6:
           for l in xrange(12):
               rainhh.append(float(inputdata[j][l*6:(l+1)*6].strip()))
        for k in xrange(12):
            line = line + "," + inputdata[j][k*6:(k+1)*6].strip()
    for j in xrange(12):
        line = line + "," + "{0:.2f}".format(rainhh[j]/3)
    for j in xrange(len(solar)):
        if lat[i]==slat[j] and lon[i] == slon[j]:
            line = line + solar[j][:-1]
    for j in xrange(len(st_name)):
        if prec[i]==st_name[j]:
            line = line + dewp[j][:-1]
    for j in xrange(len(st_name)):
        if prec[i]==st_name[j]:
            line = line + wind[j][:-1]
    fname.write(line + "\n")
fname.close()
