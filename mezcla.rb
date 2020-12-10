#Carlos ALfonso Barron Rivera
def mezcla(lista)

    if(lista.length > 1)
        mitad = lista.length / 2
        mitadIzquierda = lista[0...mitad]
        mitadDerecha = lista[mitad...lista.length]
        mezcla(mitadIzquierda)
        mezcla(mitadDerecha)
        i=0
        j=0
        k=0
        while i < mitadIzquierda.length && j < mitadDerecha.length
            if (mitadIzquierda[i] < mitadDerecha[j])
                lista[k]=mitadIzquierda[i]
                puts " anadiendo : #{mitadIzquierda[i]}"
                i=i+1
            else
                puts " anadiendo : #{mitadDerecha[j]}"
                lista[k]=mitadDerecha[j]
                j=j+1
            end
            k=k+1
        end
        while i < mitadIzquierda.length
            puts " anadiendo : #{mitadIzquierda[i]}"
            lista[k]=mitadIzquierda[i]
            i=i+1
            k=k+1
        end
        while j < mitadDerecha.length
            puts " anadiendo : #{mitadDerecha[j]}"
            lista[k]=mitadDerecha[j]
            j=j+1
            k=k+1
        end
    end
 return lista

end

content = File.read("datos.txt") # lee el archivo
lineas = content.split("\n") # divide el contenido en líneas
lista = [54,26,93,885,17,77,31,44,55,20,1,766,19,276]
start = Time.now

lista1 = mezcla(lista)

finish = Time.now
diff = finish - start
puts " tiempo  de ejecucion : #{diff}"

# lista1.each_with_index do |element, index|
#     puts "#{index}: #{element}"
# end
