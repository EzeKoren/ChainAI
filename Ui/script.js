window.onload = function() {
    var main = new Vue({
        el: '#main',
        data: {
            currentActivity: 'home'
        }
    });
}

Vue.component('button-ndea', {
    //props: ['bolitas', 'cord'],
    template: '<div class="col s2"><a class="waves-effect waves-light btn></a></div>'
})

Vue.component('game-grid', {
    template: '<div class="row"><button-ndea></button-ndea></div>'
})