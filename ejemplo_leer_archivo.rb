#Carlos alfonso Barron Rivera
start = Time.now
content = File.read("20M.txt") # lee el archivo
lineas = content.split("\n") # divide el contenido en líneas


puts "el array tiene : #{lineas.length}"
finish = Time.now
diff = finish - start
puts " tiempo  de ejecucion : #{diff.round(3)}"
# recorre las líneas y las imprime
#5.times do |i|
  #puts lines[i]
#end
