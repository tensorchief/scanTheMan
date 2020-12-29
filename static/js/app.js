Vue.component('scan-button', {
    props: ['title'],
    template: '<a href="/api/v1.0/scan">{{ title }}</a>'
})

var app = new Vue({
    el: '#app',
    data: {
        who: 'Snapper'
    }
})