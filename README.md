# Spiders
FlightSpider


Crawler made on Scrapy that pulls prices and other info from decolar website and loads in a mysql database

*used Splash to render Javascript
*Also a version of a pipeline with SQLite3

*Example 
Origem Destino
CWB - Curitiba|POA - Porto Alegre -> POA - Porto Alegre|CWB - Curitiba
FOR - Fortaleza -> GRU - São Paulo
GRU - São Paulo -> GYN - Goiania
GYN - Goiania -> GRU - São Paulo
GRU - São Paulo -> GYN - Goiania
GYN - Goiania -> GRU - São Paulo
GRU - São Paulo -> GYN - Goiania
CWB - Curitiba -> POA - Porto Alegre
POA - Porto Alegre -> CWB - Curitiba
SDU - Rio de Janeiro|CGH - São Paulo -> CGH - São Paulo|GIG - Rio de Janeiro
GIG - Rio de Janeiro|GRU - São Paulo -> GRU - São Paulo|GIG - Rio de Janeiro
GRU - São Paulo -> JPA - Joao Pessoa
REC - Recife -> GRU - São Paulo
GRU - São Paulo -> JPA - Joao Pessoa
GRU - São Paulo -> SSA - Salvador
GIG - Rio de Janeiro|GRU - São Paulo -> GRU - São Paulo|SDU - Rio de Janeiro
SDU - Rio de Janeiro|GRU - São Paulo -> CGH - São Paulo|GIG - Rio de Janeiro
CGH - São Paulo|CNF - Belo Horizonte|GIG - Rio de Janeiro -> CNF - Belo Horizonte|GIG - Rio de Janeiro|SSA - Salvador
CGH - São Paulo|CNF - Belo Horizonte|GIG - Rio de Janeiro|SSA - Salvador -> CNF - Belo Horizonte|GIG - Rio de Janeiro|SSA - Salvador|CGH - São Paulo
SSA - Salvador -> GIG - Rio de Janeiro
