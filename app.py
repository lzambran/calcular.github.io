from flask import Flask, render_template, request,flash,url_for,redirect

app = Flask(__name__)
app.secret_key = "clave_secreta"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def resultado():
    if request.method == 'POST':
      
      t= 2.064 
      # Pedir al usuario que ingrese los pretest separados por comas
      pretest = list(map(float, request.form['pretest'].split(',')))
      posttest = list(map(float, request.form['posttest'].split(',')))
      mean_pre = sum(pretest) / len(pretest)
      mean_post = sum(posttest) / len(posttest)
      mean_diff = mean_post - mean_pre
      #VARIABLES DECLARADAS PARA PODER MOSTRAR LOS VALORES AL ELEGIR (n)
      alpha = 0.05 # Valor de ejemplo
      trust_level = 0.95 # Valor de ejemplo
      std_dev_diff = ((sum((x - y - mean_diff) ** 2 for x, y in zip(pretest, posttest)) / (len(posttest) - 1)) ** 0.05)
      margen_de_error = round(t * std_dev_diff)
      n =len(pretest)
      std_dev = 0
      error_st = std_dev / (n ** alpha)
      intervalo_confianza = (mean_pre - t*error_st, mean_pre + t*error_st)
      límite_inferior = intervalo_confianza[0]
      límite_superior = intervalo_confianza[1]
      interpretation = "Con un nivel de confianza del {}% y un margen de error del {}%".format(int(trust_level*100), int((alpha)*100))

      if pretest == posttest:
         message ="No hay una diferencia significativa entre el pretest y el posttest porque las medias son iguales."
         return render_template("index.html", message=message)
        # return 'No hay una diferencia significativa entre el pretest y el posttest porque las medias son iguales.'
      elif mean_diff == 0:
          message = "No hay diferencias significativas porque las medias son iguales"
          return render_template("/", message=message)
        # return "No hay diferencias significativas porque las medias son iguales"
      else:
        respuesta = request.form['respuesta']
        #SI ELIGE (s) ENTONCES ENTRARA A LAS CONDICIONALES Y PREGUNTARA 
        if respuesta.lower() not in  ['s', 'n']:
            message = "La respuesta no es válida. Por favor, ingrese S o N."
            return render_template("index.html", message=message)
            # return 'La respuesta no es válida. Por favor, ingrese S o N.'
        if respuesta.lower() == 'n':
            # Pedir al usuario que ingrese el valor de alpha
            alpha = float(request.form['alpha'])
            #Pedir al usuario que ingrese el valor de trust_level
            trust_level = float(request.form['trust_level'])
        else:
            alpha = 0.05 # Valor de ejemplo
            trust_level = 0.95 # Valor de ejemplo
            # Calcular la media de los pretest
            mean_pre = sum(pretest) / len(pretest)
            mean_post = sum(posttest) / len(posttest)
            # Calcular la desviación estándar de los pretest
            std_dev = 0
            for dato in pretest:
               std_dev += (dato - mean_pre) ** 2
            std_dev = (std_dev / (len(pretest) - 1)) ** alpha
            # Calcular el intervalo de confianza
            n =len(pretest)
            error_st = std_dev / (n ** alpha)
            t = 2.064 
            intervalo_confianza = (mean_pre - t*error_st, mean_pre + t*error_st)
            # Calcular el límite inferior y superior
            límite_inferior = intervalo_confianza[0]
            límite_superior = intervalo_confianza[1]
            #Calcular la diferencia entre de desviación estántar de prestest y posttest
            std_dev_diff = ((sum((x - y - mean_diff) ** 2 for x, y in zip(pretest, posttest)) / (len(posttest) - 1)) ** 0.05)
            #margen de error
            margen_de_error = round(t * std_dev_diff)

            interpretation = " Con un nivel de confianza del {}% y un margen de error del {}%".format(int(trust_level*100), int((alpha)*100))
            if mean_post < límite_inferior:
                message = "Se asume que hay diferencias significativas entre el prestest y posttest, La media del posttest está significativamente por debajo  del intervalo de confianza (límite inferior). Es decir que el resultado del posttest es significativamente menor que el del pretest."
                return render_template("index.html", message=message)
                # return "Se asume que hay diferencias significativas entre el prestest y posttest, La media del posttest está significativamente por debajo  del intervalo de confianza (límite inferior). Es decir que el resultado del posttest es significativamente menor que el del pretest."
            elif mean_post > límite_superior:
                message = "Se asume que hay diferencias significativas entre el prestest y posttest. La media del posttest está significativamente por encima  del intervalo de confianza (límite superior). Es decir que el resultado del posttest es significativamente mayor que el del pretest."
                return render_template("index.html", message=message)
                # return "Se asume que hay diferencias significativas entre el prestest y posttest. La media del posttest está significativamente por encima  del intervalo de confianza (límite superior). Es decir que el resultado del posttest es significativamente mayor que el del pretest."
            else:
                interpretation += f"No se puede afirmar que haya una diferencia significativa entre el pretest y el posttest, dado que la diferencia entre la medias del posttest se encuentra dentro del intervalo de confianza."
            return render_template("result.html",interpretation=interpretation,t=t,mean_pre=mean_pre,mean_post=mean_post, mean_diff=mean_diff,std_dev_diff=std_dev_diff,margen_de_error=margen_de_error,límite_inferior=límite_inferior,límite_superior=límite_superior,trust_level=trust_level,intervalo_confianza=intervalo_confianza,alpha=alpha,respuesta=respuesta,resultado=resultado,)
    else: 
        return render_template("/",)
    return render_template("result.html",interpretation=interpretation,límite_inferior=límite_inferior,límite_superior=límite_superior,intervalo_confianza=intervalo_confianza,margen_de_error=margen_de_error,std_dev_diff=std_dev_diff,t=t,mean_pre=mean_pre,mean_post=mean_post, mean_diff=mean_diff,trust_level=trust_level,alpha=alpha,respuesta=respuesta,)


if __name__ == '__main__':
    app.run(debug=True)