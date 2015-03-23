---
layout: post
title:  "Como criar um blog no Github utilizando o Jekyll!"
date:   2015-03-23
categories: Jekyll Blog
banner_image: post1/banner.jpg
comments: true
share: true
---
###Introdução
É bem comum na área de TI e afins, as pessoas criarem um blog para registar seu processo de aprendizagem, isso é uma prática bem comum, e muito bem visto pela comunidade, por sinal. Então nesse post vou ensinar como criar um blog utilizando o Jekyll e o próprio Github, exatamente como o que eu estou usando.

###Tecnologias
Para fazermos o blog vamos usar o Github, em uma explicação bem simples, ele é um serviço de hospedagem compartilhada para projetos que usam o controle de versionamento Git. Se você não sabe o que é o Github e o Git, você precisa sair da caverna e olhar um pouco o que está acontecendo.

Também utilizamos o Jekyll que é um gerador de códigos estáticos, ou seja, não vamos precisar de ter um banco de dados para nada, todo nosso conteúdo estará alocado em cada arquivo.

Para escrevermos de fato os posts, vamos utilizar o Markdown, que é uma linguagem de marcação bem simples (mais simples que o HTML).

###Configurando o ambiente
(Atualmente) Eu estou usando o Ubuntu como máquina de trabalho, então todas as configurações serão para uma máquina com esse SO. Caso você esteja usando outro, indico que você siga os passos tentando adequar para o seu sistema. Antes de instalarmos o necessário para tal, vamos dar uma pesquisada em um tema para nosso blog. 

*Seja original, não copie seu coleguinha.*

Com uma simples busca no google com as palavras chave `jekyll theme` e já vamos encontrar muito conteúdo, ou podemos acessar o [link](https://github.com/jekyll/jekyll/wiki/Themes), onde há uma lista bem grande de temas. Após encontrarmos, podemos dar um `fork` no projeto e baixarmos para nossa máquina com `git clone`. Agora sim, vamos lá:

Instale o ruby:

{% highlight bash %}
sudo apt-get install ruby-full
{% endhighlight %}

Instale o bundler (é ele quem cuida das dependências do projeto):

{% highlight bash %}
sudo gem install bundler
{% endhighlight %}

Estando dentro da pasta do projeto:

{% highlight bash %}
bundle install
{% endhighlight %}

Agora sim, já podemos começar a trabalhar nas configurações do nosso blog. Dentro dele terá um arquivo chamado `_config.yml`. Abra-o e faça as alterações necessárias, são bem simples, a maioria são alto explicativas. Se deseja ver um exemplo de como deve ficar esse arquivo, acesse esse [link](https://github.com/MarcosDias/blog/blob/master/_config.yml) e veja como está a configuração desse blog.

Dentro da pasta `_post` provavelmente terá alguns posts de exemplo. Particularmente eu joguei todo esse conteúdo para uma outra pasta, apenas para ter arquivos de exemplo. Seguindo esses arquivos, você consegue facilmente criar suas postagem sem dificuldades.

Podemos acompanhar como está nosso blog rodando o Jekyll localmente, com o seguinte comando:

{% highlight bash %}
bundle exec jekyll serve
{% endhighlight %}

E o mais legal, as alterações feitas enquanto o servidor estiver ativo também serão refletidas, ou seja, não é necessário ficarmos rodando esse comando a cada alteração.

### Subindo para o GitHub
Agora, estamos quase finalizando. Suba todo o código para o GitHub, vá em Settings e repare que o Github altomagicamente criou nossa página, mas ao clicarmos no link vemos que ela não sofreu as alterações que nós fizemos. 
![Setting GitHub](https://raw.githubusercontent.com/MarcosDias/blog/master/assets/images/post1/github-settings.png)
Isso acontece pois o GitHub fica observando a branch `gh-pages` e não a `master` do nosso repositório. Para resolvermos isso, temos que entrar na branch `gh-pages`, e dar um `merge` com a branch `master` e subir novamente para o GitHub.


Agora sim, temos a nossa página ar.

Viu como é simples. :)

Segue de exemplo o link do GitHub desse post:

[https://github.com/MarcosDias/blog/blob/master/_posts/2015-03-18-criando-um-blog-github-utlizando-jekyll.md](https://github.com/MarcosDias/blog/blob/master/_posts/2015-03-18-criando-um-blog-github-utlizando-jekyll.md)