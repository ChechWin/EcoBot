import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'Ha iniciado sesión como {bot.user}')

@bot.command(name='eco' or "ayuda")
async def saluda(ctx):
    await ctx.send('¡Hola! Soy EcoBot, un asistente virtual que te ayudará a aprender más sobre prácticas ecológicas y formas de reducir los residuos. ¿En qué puedo ayudarte hoy?')
    await ctx.send('**Opciones disponibles:**')
    await ctx.send('$practicas - Prácticas ecológicas para implementar en tu vida diaria')
    await ctx.send('$reducir_residuos - Consejos para reducir los residuos en tu hogar y comunidad')
    await ctx.send('$reciclaje - Cómo reciclar correctamente y qué materiales se pueden reciclar')
    await ctx.send('$transporte - Sugerencias para reducir el impacto ambiental del transporte')
    await ctx.send('$alimentación - Consejos para una alimentación más sostenible y saludable')
    await ctx.send('$agua - Sugerencias para ahorrar agua y reducir el consumo')
    await ctx.send('$energía - Consejos para reducir el consumo de energía y utilizar fuentes renovables')
    await ctx.send('$jardinería - Sugerencias para crear un jardín ecológico y sostenible')
    await ctx.send('$noticias - Obtener noticias y actualizaciones sobre temas ambientales.')
    await ctx.send('$ayuda - Mostrar esta lista de opciones nuevamente')

@bot.command(name='practicas')
async def practicas_ecologicas(ctx):
    mensaje = "*Prácticas ecológicas para implementar en tu vida diaria:**\n"
    mensaje += "1. **Reducir el consumo de plásticos**: Evita usar bolsas de plástico, botellas de agua y otros productos que generen residuos.\n"
    mensaje += "2. **Utilizar bolsas reutilizables**: Lleva tus propias bolsas cuando vayas de compras.\n"
    mensaje += "3. **Ahorrar agua**: Cierra el grifo mientras te lavas las manos o te duchas.\n"
    mensaje += "4. **Reciclar**: Separa tus residuos y recicla papel, plástico, vidrio y metal.\n"
    mensaje += "5. **Utilizar transporte público o bicicleta**: Reduce el uso de tu vehículo y opta por transporte público o bicicleta."
    await ctx.send(mensaje)

@bot.command(name='reducir_residuos')
async def reducir_residuos(ctx):
    mensaje = "*Consejos para reducir los residuos en tu hogar y comunidad:*\n"
    mensaje += "1. **Reducir el consumo de productos con envases**: Opta por productos con envases biodegradables o reutilizables.\n"
    mensaje += "2. **Utilizar contenedores de reciclaje**: Separa tus residuos y utiliza contenedores de reciclaje.\n"
    mensaje += "3. **Compostar**: Convierte tus residuos orgánicos en abono para tu jardín.\n"
    mensaje += "4. **Donar o vender objetos que no se utilizan**: No deseches objetos que aún pueden ser útiles.\n"
    mensaje += "5. **Participar en programas de reciclaje comunitarios**: Únete a programas de reciclaje en tu comunidad."
    await ctx.send(mensaje)

@bot.command(name='reciclaje')
async def reciclaje(ctx):
    mensaje = "*Cómo reciclar correctamente y qué materiales se pueden reciclar:*\n "
    mensaje += "1. **Papel y cartón**: Recicla papel, cartón y otros materiales de papel.\n "
    mensaje += "2. **Plásticos**: Recicla plásticos como botellas de agua, bolsas de plástico y otros productos.\n"
    mensaje += "3. **Vidrio**: Recicla vidrio de botellas y otros objetos.\n"
    mensaje += "4. **Metal**: Recicla metal de latas, botellas y otros objetos.\n"
    mensaje += "5. **Electrónicos**: Recicla dispositivos electrónicos como teléfonos, computadoras y otros.\n"
    await ctx.send(mensaje)

@bot.command(name='transporte')
async def transporte(ctx):
    mensaje = "*Sugerencias para reducir el impacto ambiental del transporte:*\n"
    mensaje += "1. **Utilizar transporte público**: Opta por autobuses, trenes y otros medios de transporte público.\n"
    mensaje += "2. **Conducir un vehículo híbrido o eléctrico**: Considera cambiar a un vehículo más ecológico.\n"
    mensaje += "3. **Compartir vehículos**: Comparte tu vehículo con amigos o familiares.\n"
    mensaje += "4. **Utilizar bicicleta o caminar**: Opta por caminar o montar bicicleta para distancias cortas.\n"
    mensaje += "5. **Planificar viajes**: Planifica tus viajes para minimizar la distancia recorrida.\n"
    await ctx.send(mensaje)

@bot.command(name='alimentación')
async def alimentacion(ctx):
    mensaje = "*Consejos para una alimentación más sostenible y saludable:*"
    mensaje += "1. *Comprar productos locales y de temporada*: Apoya a productores locales y reduce el transporte de alimentos.\n"
    mensaje += "2. *Reducir el consumo de carne*: Considera reducir tu consumo de carne para reducir la huella de carbono.\n"
    mensaje += "3. *Utilizar productos sin envases*: Opta por productos sin envases o con envases biodegradables.\n"
    mensaje += "4. *Preparar comidas en casa*: Prepara comidas en casa para reducir el consumo de envases y residuos.\n"
    mensaje += "5. *Reducir el desperdicio de alimentos*: Planea tus comidas y evita desperdiciar alimentos.\n"
    await ctx.send(mensaje)

@bot.command(name='agua')
async def agua(ctx):
    mensaje = "*Sugerencias para ahorrar agua y reducir el consumo:*\n"
    mensaje += "1. *Utilizar dispositivos de bajo flujo*: Instala dispositivos de bajo flujo en tus grifos y duchas.\n"
    mensaje += "2. *Reparar fugas*: Repara fugas de agua para evitar desperdicio.\n"
    mensaje += "3. *Utilizar agua de lluvia*: Utiliza agua de lluvia para regar tus plantas y limpiar superficies.\n"
    mensaje += "4. *Reducir el tiempo de ducha*: Reduce el tiempo de ducha para ahorrar agua.\n"
    mensaje += "5. *Utilizar un medidor de agua*: Utiliza un medidor de agua para monitorear tu consumo.\n"
    await ctx.send(mensaje)

@bot.command(name='energía')
async def energia(ctx):
    mensaje = "*Consejos para reducir el consumo de energía y utilizar fuentes renovables:*\n"
    mensaje += "1. *Utilizar bombillas LED*: Cambia a bombillas LED para reducir el consumo de energía.\n"
    mensaje += "2. *Apagar electrodomésticos cuando no estén en uso*: Apaga electrodomésticos y luces cuando no estén en uso.\n"
    mensaje += "3. *Utilizar paneles solares*: Considera instalar paneles solares para generar energía renovable.\n"
    mensaje += "4. *Reducir el consumo de energía en la noche*: Reduce el consumo de energía en la noche apagando luces y electrodomésticos.\n"
    mensaje += "5. *Utilizar un medidor de energía*: Utiliza un medidor de energía para monitorear tu consumo.\n"
    await ctx.send(mensaje)
    
@bot.command(name='jardineria')
async def jardineria(ctx):
    mensaje = "*Sugerencias para crear un jardín ecológico y sostenible:*\n"
    mensaje += "1. *Utilizar plantas nativas*: Utiliza plantas nativas que requieren menos agua y mantenimiento.\n"
    mensaje += "2. *Reducir el uso de pesticidas y fertilizantes*: Utiliza métodos naturales para controlar plagas y fertilizar tu jardín.\n"
    mensaje += "3. *Utilizar compost*: Utiliza compost para fertilizar tu jardín y reducir residuos.\n"

@bot.command(name='noticias')
async def noticias(ctx):
    mensaje = ""
    mensaje += "*Noticias ambientales recientes:*\n "
    mensaje += "• La contaminación del aire mata a 7 millones de personas al año\n "
    mensaje += "• El cambio climático es responsable del 20% de las muertes en el mundo\n "
    mensaje += "• La deforestación es responsable del 15% de las emisiones de gases de efecto invernadero\n "
    mensaje += "*Para obtener más noticias ambientales actualizadas, visita:*\n "
    mensaje += "https://www.bbc.com/mundo/topics/cjgn709jk16t"
    await ctx.send(mensaje)

bot.run("")
