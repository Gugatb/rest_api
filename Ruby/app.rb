
require 'sinatra'

# Definir a porta.
set :port, 8080

# Exibir o ola mundo.
# Author: Gugatb
# Date: 17/06/2018
get '/' do
  'Ola mundo'
end

# Exibir os parametros.
# Author: Gugatb
# Date: 17/06/2018
get '/param' do
  {'Key1' => params['key1'], 'Key2' => params['key2']}.to_json
end

# Exibir o texto.
# Author: Gugatb
# Date: 15/06/2018
# Param: value o valor
get '/text/:text' do
  params[:text]
end
