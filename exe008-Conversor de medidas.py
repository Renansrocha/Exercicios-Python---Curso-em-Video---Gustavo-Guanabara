distancia= float(input('Digite uma distancia em metros: '))
km= distancia/1000
hec= distancia/100
cm= distancia*100
mm= distancia*1000
print ("A medida de {:.0f} metros corresponde a: {:.1f}km, {:.1f}hec, {:.0f}cm e {:.0f}mm".format(distancia,km,hec,cm,mm))
