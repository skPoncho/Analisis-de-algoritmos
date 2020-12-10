#Carlos ALfonso Barron Rivera
#analisis de algoritmos
def ord_2_arrays(lista1,lista2)
    lista_res = []
    i = 0
    j = 0
    veces = lista1.length + lista2.length
    veces.times do |num|
        #puts "  #{lista1[i]} <    #{lista2[j]} "
        if(i < lista1.length)
          if(lista1[i] <  lista2[j])
            lista_res.push(lista1[i])
            i = i + 1
          else
            lista_res.push(lista2[j])
            j = j + 1
          end
        else
          lista_res.push(lista2[j])
        end
    end
    lista_res.each do |num|
      puts num
    end
end

#content = File.read("datos.txt") # lee el archivo
#lineas = content.split("\n") # divide el contenido en líneas
lista = [0,2,4,6,8,14,19]
lista2 = [1,3,5,7,9,18,27]


start = Time.now
ord_2_arrays(lista,lista2)


finish = Time.now
diff = finish - start
puts " tiempo  de ejecucion : #{diff}"
