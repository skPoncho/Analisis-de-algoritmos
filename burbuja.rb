#Carlos ALfonso Barron Rivera
def ordenamientoBurbuja(lista)

    lista.each do |num|
        (lista.length-1).times do |i|
          if(lista[i]>lista[i+1])
            temp = lista[i]
            lista[i] = lista[i+1]
            lista[i+1] = temp
          end
      end
    end
    lista.each do |num|
      puts num
    end

end


content = File.read("datos.txt") # lee el archivo
lineas = content.split("\n") # divide el contenido en líneas
lista = [54,26,93,17,32,25,76,2,3,65,776,6,87,69,64,119,885,887,220]

start = Time.now
ordenamientoBurbuja(lista)

#puts "el array tiene : #{lineas.length}"
finish = Time.now
diff = finish - start
puts " tiempo  de ejecucion : #{diff}"
