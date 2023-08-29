{
 "metadata": {
  "name": "",
  "signature": "sha256:2a21a8f661b1b3ee32110d838ed4bc590839afdb44cdb608c18b4e920277b99e"
 },
 "nbformat": 3,
 "nbformat_minor": 0,
 "worksheets": [
  {
   "cells": [
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "# Ejercicios 2014/09/24"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "## Archivos y Matrices\n",
      "\n",
      "Calcule la nota final de cada alumno, suponiendo que existen dos archivos con datos:\n",
      "\n",
      "#### `notas.txt`\n",
      "\n",
      "- Cada l\u00ednea representa las notas de un alumno\n",
      "- Cada l\u00ednea contiene las notas en los ejercicios del a\u00f1o del respectivo alumno, separadas por espacio.\n",
      "\n",
      "Ejemplo:\n",
      "\n",
      "    7.0 6.5 3.5 4.3\n",
      "    3.0 5.5 6.5 4.1\n",
      "    5.0 2.5 5.5 4.5\n",
      "    ...\n",
      "\n",
      "\n",
      "#### `ponderacion.txt`\n",
      "\n",
      "- Contiene una l\u00ednea con las ponderaciones de los ejercicios, en n\u00fameros de 0 a 100\n",
      "\n",
      "Ejemplo:\n",
      "\n",
      "    20 20 20 40"
     ]
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "from numpy import *\n",
      "\n",
      "def calc_notas(f1, f2):\n",
      "    \n",
      "    lista_aux = []                   #creamos una lista con forma de matriz\n",
      "    for line in open(f1).readlines():\n",
      "        fila = []\n",
      "        for nota in line.split():\n",
      "            fila.append(float(nota))\n",
      "        lista_aux.append(fila)\n",
      "\n",
      "    matrix_notas = matrix(lista_aux) #creamos un objeto matrix de numpy\n",
      "\n",
      "    ponderaciones = open(f2).readline().split()\n",
      "    \n",
      "    lista_aux = []                   #creamos una lista con forma de matriz\n",
      "    for ponderacion in ponderaciones:\n",
      "        lista_aux.append([float(ponderacion)])\n",
      "    \n",
      "    matrix_ponderaciones = matrix(lista_aux)    \n",
      "    \n",
      "    print matrix_notas * matrix_ponderaciones / 100.0"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 1
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "## Funci\u00f3n ocultar palabra\n",
      "\n",
      "Escriba una funci\u00f3n que reciba una palabra y retorne un string solamente con letras \"X\", del mismo largo de la palabra."
     ]
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "def ocultar(palabra):\n",
      "    aux = \"\"\n",
      "    for i in range(len(palabra)):\n",
      "        aux+=\"X\"\n",
      "    return aux\n",
      "\n",
      "def ocultar(palabra):\n",
      "    return \"X\" * len(palabra)\n"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 2
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "## Censurar palabras en una frase (M\u00e9todos para recorrer listas)\n",
      "\n",
      "Suponga que existe un arreglo con palabras \"prohibidas\". Escriba una funci\u00f3n que reciba un texto y reemplace todas las palabras prohibidas con letras \"X\". Considere que no vienen signos de puntuaci\u00f3n en el texto, ni espacios innecesarios."
     ]
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "def censurar(texto, palabras_prohibidas): #sin usar replace\n",
      "    aux = \"\"\n",
      "    for palabra in texto.split(\" \"):\n",
      "        if palabra not in palabras_prohibidas:\n",
      "            aux += palabra + \" \"\n",
      "        else:\n",
      "            aux += ocultar(palabra) + \" \"\n",
      "    return aux.strip()\n",
      "\n",
      "\n",
      "def censurar(texto, palabras_prohibidas): #usando replace\n",
      "    for palabra in palabras_prohibidas:\n",
      "        texto = texto.replace(palabra, ocultar(palabra))\n",
      "    return texto\n"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 3
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "**Tiene un problema:**\n",
      "\n",
      "Ejemplo: dado el texto \"`PAN PANADERIA`\" y la lista de palabras prohibidas `[\"PAN\", \"PANADERIA\"]`, la primera versi\u00f3n retorna \"`XXX XXXXXXXXX`\" y la segunda versi\u00f3n retorna \"`XXX XXXADERIA`\""
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "## Cambiar letras en un string (iterar dentro de un string)\n",
      "(Convertir texto en arreglo y viceversa)\n",
      "\n",
      "Leet speak o leet (1337 5p34k o 1337 en la escritura leet) es un tipo de escritura compuesta de caracteres alfanum\u00e9ricos, es usada por algunas comunidades y usuarios de diferentes medios de internet. Esta escritura es caracterizada por escribir caracteres alfanum\u00e9ricos de una forma incomprensible para otros usuarios ajenos, inexpertos o ne\u00f3fitos a los diferentes grupos que utilizan esta escritura.\n",
      "\n",
      "Escriba una funci\u00f3n que reciba un string y retorne un nuevo string en donde se reemplace todas las letras \"E\" may\u00fascula o min\u00fascula por un n\u00famero 3."
     ]
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "def leet(texto): #usando un string auxiliar\n",
      "    aux=\"\"\n",
      "    for letra in texto:\n",
      "        if letra==\"E\" or letra==\"e\": aux+=\"3\"\n",
      "        else: aux+=letra\n",
      "    return aux\n",
      "\n",
      "def leet(texto): #usando una lista auxiliar, y reemplazando \"in-place\"\n",
      "    aux = list(texto)\n",
      "    for i in range(len(aux)):\n",
      "        if aux[i]==\"E\" or aux[i]==\"e\": aux[i]=\"3\"\n",
      "    return \"\".join(aux)\n",
      "    \n",
      "def leet(texto): #usando funcion \"replace\"\n",
      "    return texto.replace(\"E\",\"3\").replace(\"e\",\"3\")"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 4
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "## Funci\u00f3n `es_vocal`\n",
      "\n",
      "Escriba una funci\u00f3n que reciba un string y responda True o False dependiendo si el string es una vocal"
     ]
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "def es_vocal(texto):\n",
      "    return texto in [\"A\", \"E\", \"I\", \"O\", \"U\", \"a\", \"e\", \"i\", \"o\", \"u\"]\n",
      "\n",
      "def es_vocal(texto):\n",
      "    return texto.upper() in [\"A\", \"E\", \"I\", \"O\", \"U\"]\n",
      "\n",
      "def es_vocal(texto):\n",
      "    return texto.upper() in \"AEIOU\" and len(texto)==1"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 5
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "## Jerigonza - c\u00f3mo recorrer una lista\n",
      "\n",
      "La jerigonza, jerigonzo o jerigoncio por una parte y el geringoso o jeringozo por otra, son dos variantes l\u00fadicas del habla en las que se intercalan s\u00edlabas entre medio de una palabra en forma reiterada. \n",
      "\n",
      "Jeringozo:\n",
      "Despu\u00e9s de cada vocal se agrega el sonido \"p\" y se repite la vocal.\n",
      "\n",
      "Ejemplo: \"Hola como estas\" => \"Hopolapa copomopo epestapas\"\n",
      "\n",
      "Implemente una funci\u00f3n que reciba un texto y entregue su representaci\u00f3n en Jeringozo."
     ]
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "def jeringozo(texto):\n",
      "    aux=\"\"\n",
      "    for letra in texto:\n",
      "        if not es_vocal(letra):\n",
      "            aux+=letra\n",
      "        else:\n",
      "            aux+=letra+\"p\"+letra\n",
      "    return aux"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 6
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "## C\u00f3mo hacer un histograma\n",
      "\n",
      "- Dado un texto, calcule cu\u00e1ntas veces se repite cada palabra\n",
      "- Dibuje un histograma en pantalla, de la forma\n",
      "\n",
      "```\n",
      "Chao     10 ##########\n",
      "Hola      5 #####\n",
      "Iorana    1 #\n",
      "```"
     ]
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "def histograma(texto):\n",
      "    contador = {}\n",
      "    for palabra in texto.split(\" \"):\n",
      "        if palabra not in contador: contador[palabra]=0\n",
      "        contador[palabra]+=1\n",
      "    #tenemos un diccionario con la cuenta de palabras\n",
      "    for palabra in sorted(contador.keys()):\n",
      "        print palabra, contador[palabra], \"#\" * contador[palabra]\n",
      "        print \"%-40s %-10s %s\"%(palabra, contador[palabra], \"#\" * contador[palabra])"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 7
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "## *Extra, bonus:* API de Twitter\n",
      "\n",
      "Haga un programa que se conecte a Twitter y muestre los \u00faltimos tweets de alg\u00fan usuario (e.g. @MedelPitbull)"
     ]
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "import twitter\n",
      "\n",
      "api = twitter.Api(consumer_key='AAAAAAAAAAAAAAAAAAAAAA',\n",
      "                  consumer_secret='BBBBBBBBBBBBBBBBBBBBBBBBBB',\n",
      "                  access_token_key='CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC',\n",
      "                  access_token_secret='DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD') \n",
      "                  #para hacer que funcione deben cambiar estos c\u00f3digos por unos nuevos. Se consiguen en el sitio de twitter.  (https://twittercommunity.com/t/how-to-get-my-api-key/7033/2)\n",
      "\n",
      "statuses = api.GetUserTimeline(screen_name=\"@MedelPitbull\")\n",
      "\n",
      "for status in statuses:\n",
      "    print status.created_at, repr(status.text)"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 8
    }
   ],
   "metadata": {}
  }
 ]
}