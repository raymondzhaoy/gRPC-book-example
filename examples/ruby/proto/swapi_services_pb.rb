# Generated by the protocol buffer compiler.  DO NOT EDIT!
# Source: swapi.proto for package 'swapi.v1'

require 'grpc'
require 'swapi_pb'

module Swapi
  module V1
    module Starwars
      class Service

        include GRPC::GenericService

        self.marshal_class_method = :encode
        self.unmarshal_class_method = :decode
        self.service_name = 'swapi.v1.Starwars'

        rpc :GetFilm, GetFilmRequest, GetFilmResponse
        rpc :ListFilms, ListFilmsRequest, ListFilmsResponse
        rpc :GetVehicle, GetVehicleRequest, GetVehicleResponse
        rpc :ListVehicles, ListVehiclesRequest, ListVehiclesResponse
        rpc :GetStarship, GetStarshipRequest, GetStarshipResponse
        rpc :ListStarships, ListStarshipsRequest, ListStarshipsResponse
        rpc :GetSpecies, GetSpeciesRequest, GetSpeciesResponse
        rpc :ListSpecies, ListSpeciesRequest, ListSpeciesResponse
        rpc :GetPlanet, GetPlanetRequest, GetPlanetResponse
        rpc :ListPlanets, ListPlanetsRequest, ListPlanetsResponse
        rpc :GetPerson, GetPersonRequest, GetPersonResponse
        rpc :ListPeople, ListPeopleRequest, ListPeopleResponse
        rpc :ListStarshipActions, ListStarshipActionsRequest, stream(StarshipAction)
      end

      Stub = Service.rpc_stub_class
    end
  end
end
