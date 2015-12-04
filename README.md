# Olho Vivo Safira

São José da Safira é uma cidade do interior de Minas Gerais com cerca de 4 mil habitantes.
Esse projeto foi criado com o intuito de oferecer a população safirense informações sobre os recursos que vem para o município.


## O que é?

    Uma plataforma de consulta de recursos que são destinados para o município.


## Como funciona?

    As informações são retiradas do portal de transparência do Governo Federal e são disponibilizadas na nossa plataforma.


## De onde vem as informações?

    * [Portal da Transparência - Recursos por estado/município](http://www.portaltransparencia.gov.br/PortalTransparenciaListaAcoes.asp?Exercicio=2015&SelecaoUF=1&SiglaUF=MG&CodMun=5259)

    * [Portal da Transparência - Convênios](http://www.portaltransparencia.gov.br/convenios/convenioslista.asp?uf=mg&codmunicipio=5259&codorgao=51000&tipoconsulta=1&periodo=)

    * [Portal da Transparência - Recursos por favorecido](http://www.portaltransparencia.gov.br/PortalTransparenciaPesquisaFavorecidoPJ_2.asp?Exercicio=2015&hidIdTipoFavorecido=&hidNumCodigoTipoNaturezaJuridica=1&textoPesquisa=&CpfCnpjNis=18409235000105&NomeFavorecido=MUNICIPIO%20DE%20SAO%20JOSE%20DA%20SAFIRA%20SAO%20JOSE%20DA%20SAFIRA%20PREF%20GABINETE%20DO%20PREFEITO&valorNatJud=&valorFavorecido=390838327&Ordem=3)

    * [Portal da Transparência - Bolsa Família](http://www.portaltransparencia.gov.br/PortalTransparenciaPesquisaAcaoFavorecido.asp?Exercicio=2015&textoPesquisa=&textoPesquisaAcao=&codigoAcao=8442&codigoFuncao=08&siglaEstado=MG&codigoMunicipio=5259)



### Fluxo de Atualização dos dados

    As informações são atualizadas diaramente.

    1 - Os dados são consultados no `Portal da Transparência - Recursos por estado/município`
        1.1 - Os detalhes da ação governamental são acessados
            1.1.1 - O favorecido é registrado
            1.1.2 - O detalhamento mensal é registrado
        1.2 - Os dados são agrupados por categoria
        1.3 - próxima página é consultada

    2 - Os dados são consultados no `Portal da Transparência - Bolsa Família`
        1.1 - O nome do favorecido é registrado e o valor total
            1.1.1 - O detalhamento mensal é registrado


