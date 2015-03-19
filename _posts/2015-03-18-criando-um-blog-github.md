---
layout: post
title:  "Como criar um blog no Github!"
date:   2015-01-01 0:00:55
categories: Jekyll Blog
banner_image: sample-banner-image-1.jpg
comments: true
share: true
---
###Introdução
É bem comum na área de TI e afins, as pessoas criarem um blog para registar seu processo de aprendizagem, isso é uma prática bem comum, e muito bem visto pela comunidade por sinal. Então nesse post vou ensinar como criar um blog utilizando o Jekyll e o próprio Github, exatamente como o que eu estou usando.

###Tecnologias
Para fazermos o blog vamos usar o Github, em uma explicação bem simples, ele é um serviço de hospedagem compartilhada para projetos que usam o controle de versionamento Git. Se você não sabe o que é o Github e o Git, você precisa sair da caverna e olhar um pouco o que está acontecendo.

Também utilizamos o Jekyll que é um gerador de códigos estáticos, ou seja, não vamos precisar de ter um banco de dados para nada, todo nosso conteudo estarrá alocado em cada arquivo.

Para escrevermos de fato os posts, vamos utilizar o Markdown, que é uma linguagem de marcação bem simples (mais simples que o HTML).

###Configurando o ambiente
(Atualmente) Eu estou usando o Ubunto como máquina de trabalho, então todas as configurações serão para uma máquina com esse SO. Caso você esteja usando outro, indico que você siga os passos tentando adequar para o seu sistema. Antes de instalarmos o necessário para tal, vamos dar uma pesquisada em um tema para nosso blog. 

*Seja original, não copie seu coleguinha.*

Com uma simples busca no google com a palavra chave `jekyll theme` e já vamos encontrar muitas coisas, ou podemos acessar o [link], onde há uma lista bem grande de temas. Após encontrarmos, podemos dar um `fork` no projeto e baixamos para nossa máquina com `git clone`. Agora sim, vamos lá:

Instale o ruby:

{% highlight bash %}
sudo apt-get install ruby-full
{% endhighlight %}

Instale o bundler (é ele quem cuida das dependêcias do projeto):

{% highlight bash %}
sudo gem install bundler
{% endhighlight %}

Estando dentro da pasta do projeto:

{% highlight bash %}
bundle install
{% endhighlight %}

Agora sim, já podemos começar a trabalhar nas configurações do nosso blog. Dentro dele terá um arquivo chamado `_config.yml`. Abra ele e faça as alterações necessárias, são bem simples, a maioria delas são alto explicativas.

