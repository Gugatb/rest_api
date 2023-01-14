
require 'sinatra'

set :port, 8080

get '/hello' do
  'Hello world!'
end

get '/param' do
  {'key1' => params['key1'], 'key2' => params['key2']}.to_json
end

get '/text/:text' do
  {'text' => params[:text]}.to_json
end
