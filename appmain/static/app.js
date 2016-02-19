(function () {
  'use strict';
  angular.module('MyApp',['ngMaterial', 'ngMessages']);
  angular.module('MyApp').controller('AutocompleteCtrl', AutocompleteCtrl);
  angular.module('MyApp').controller('ResultCtrl', ResultCtrl);
  var requestChanged = "requestChanged";

  function AutocompleteCtrl ($timeout, $q, $log, $http, $rootScope) {
    var self = this;

    self.simulateQuery = false;
    self.isDisabled    = false;

    self.querySearch   = getHttpResponse;
    self.selectedItemChange = selectedItemChange;
    self.searchTextChange   = searchTextChange;

    function searchTextChange(text) {
      $log.info('Text changed to ' + text);
    }

    function selectedItemChange(item) {
      $log.info('Item changed to ' + JSON.stringify(item));
      $rootScope.$broadcast(requestChanged, { value: item });
    }

    function getHttpResponse(query) {
      var deferred = $q.defer();
      var lowercaseQuery = angular.lowercase(query);

      $http({
        method : "GET",
        url : "search/city/" + lowercaseQuery,
      }).then(function mySucces(response) {
        deferred.resolve(response.data.list);
        $log.info(response.data.list);
      }, function myError(response) {
        deferred.resolve([]);
        $log.info(response);
      });

      return deferred.promise;
    }
  }


  function ResultCtrl ($http, $log, $rootScope) {
    var self = this;

    self.books = []

    $rootScope.$on(requestChanged, function (event, data) {
        if (data.value === undefined) {
          self.books = []
          return;
        }

        $http({
          method : "GET",
          url : "search/book/" + data.value,
        }).then(function mySucces(response) {
          self.books = response.data.list;
          $log.info(response.data.list);
        }, function myError(response) {
          $log.info(response);
        });
    });

  }

})();
