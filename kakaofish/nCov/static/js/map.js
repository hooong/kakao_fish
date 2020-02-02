var mapOptions = {
    center: new naver.maps.LatLng(37.340412, 127.339595),
    zoom: 4
};

var map = new naver.maps.Map('map', mapOptions);

// 1번확진자
var polyline_1 = new naver.maps.Polyline({
    map: map,
    path: [
        new naver.maps.LatLng(37.461439, 126.447600),
        new naver.maps.LatLng(37.478415, 126.668536)
    ],
    clickable: true,
    strokeColor: '#5347AA',
    strokeStyle: 'shortdash',
    strokeOpacity: 0.6,
    strokeWeight: 5
});
var circle = new naver.maps.Circle({
    map: map,
    center: new naver.maps.LatLng(37.461439, 126.447600),
    radius: 4000,
    fillColor: '#E51D1A',
    fillOpacity: 0.3
});
var circle = new naver.maps.Circle({
    map: map,
    center: new naver.maps.LatLng(37.478415, 126.668536),
    radius: 1000,
    fillColor: '#E51D1A',
    fillOpacity: 0.3
});
naver.maps.Event.addListener(polyline_1, 'mouseover', function() {
    polyline_1.setOptions({
        strokeColor: '#E51D1A',
        strokeStyle: 'solid',
        strokeOpacity: 1
    });
});
naver.maps.Event.addListener(polyline_1, 'mouseout', function() {
    polyline_1.setOptions({
        strokeColor: '#5347AA',
        strokeStyle: 'shortdash',
        strokeOpacity: 0.5
    });
});


// 2번확진자
var polyline_2 = new naver.maps.Polyline({
    map: map,
    path: [
        new naver.maps.LatLng(37.559660, 126.803975),
        new naver.maps.LatLng(37.606522, 127.015286),
        new naver.maps.LatLng(37.567228, 127.005552)
    ],
    clickable: true,
    strokeColor: '#5347AA',
    strokeStyle: 'shortdash',
    strokeOpacity: 0.5,
    strokeWeight: 5
});
var circle = new naver.maps.Circle({
    map: map,
    center: new naver.maps.LatLng(37.559660, 126.803975),
    radius: 1000,
    fillColor: '#8000FF',
    fillOpacity: 0.3
});
var circle = new naver.maps.Circle({
    map: map,
    center: new naver.maps.LatLng(37.606522, 127.015286),
    radius: 1000,
    fillColor: '#8000FF',
    fillOpacity: 0.3
});
var circle = new naver.maps.Circle({
    map: map,
    center: new naver.maps.LatLng(37.567228, 127.005552),
    radius: 1000,
    fillColor: '#8000FF',
    fillOpacity: 0.3
});
naver.maps.Event.addListener(polyline_2, 'mouseover', function() {
    polyline_2.setOptions({
        strokeColor: '#8000FF',
        strokeStyle: 'solid',
        strokeOpacity: 1
    });
});
naver.maps.Event.addListener(polyline_2, 'mouseout', function() {
    polyline_2.setOptions({
        strokeColor: '#5347AA',
        strokeStyle: 'shortdash',
        strokeOpacity: 0.5
    });
});

// 3번확진자
var polyline_3 = new naver.maps.Polyline({
    map: map,
    path: [
        new naver.maps.LatLng(37.642035, 126.831015),
        new naver.maps.LatLng(37.679255, 126.763464),
        new naver.maps.LatLng(37.511039, 127.039706),
    ],
    clickable: true,
    strokeColor: '#5347AA',
    strokeStyle: 'shortdash',
    strokeOpacity: 0.5,
    strokeWeight: 5
});
var circle = new naver.maps.Circle({
    map: map,
    center: new naver.maps.LatLng(37.679255, 126.763464),
    radius: 1000,
    fillColor: '#04B45F',
    fillOpacity: 0.3
});
var circle = new naver.maps.Circle({
    map: map,
    center: new naver.maps.LatLng(37.511039, 127.039706),
    radius: 2000,
    fillColor: '#04B45F',
    fillOpacity: 0.3
});
var circle = new naver.maps.Circle({
    map: map,
    center: new naver.maps.LatLng(37.642035, 126.831015),
    radius: 1000,
    fillColor: '#04B45F',
    fillOpacity: 0.3
});
naver.maps.Event.addListener(polyline_3, 'mouseover', function() {
    polyline_3.setOptions({
        strokeColor: '#04B45F',
        strokeStyle: 'solid',
        strokeOpacity: 1
    });
});
naver.maps.Event.addListener(polyline_3, 'mouseout', function() {
    polyline_3.setOptions({
        strokeColor: '#5347AA',
        strokeStyle: 'shortdash',
        strokeOpacity: 0.5
    });
});

// 4번확진자
var polyline_4 = new naver.maps.Polyline({
    map: map,
    path: [
        new naver.maps.LatLng(37.461439, 126.447600),
        new naver.maps.LatLng(37.027377, 127.108912),
        new naver.maps.LatLng(37.351316, 127.123325)
    ],
    clickable: true,
    strokeColor: '#5347AA',
    strokeStyle: 'shortdash',
    strokeOpacity: 0.5,
    strokeWeight: 5
});
var circle = new naver.maps.Circle({
    map: map,
    center: new naver.maps.LatLng(37.461439, 126.447600),
    radius: 3000,
    fillColor: '#8A4B08',
    fillOpacity: 0.3
});
var circle = new naver.maps.Circle({
    map: map,
    center: new naver.maps.LatLng(37.027377, 127.108912),
    radius: 6500,
    fillColor: '#8A4B08',
    fillOpacity: 0.3
});
var circle = new naver.maps.Circle({
    map: map,
    center: new naver.maps.LatLng(37.351316, 127.123325),
    radius: 1000,
    fillColor: '#8A4B08',
    fillOpacity: 0.3
});
naver.maps.Event.addListener(polyline_4, 'mouseover', function() {
    polyline_4.setOptions({
        strokeColor: '#8A4B08',
        strokeStyle: 'solid',
        strokeOpacity: 1
    });
});
naver.maps.Event.addListener(polyline_4, 'mouseout', function() {
    polyline_4.setOptions({
        strokeColor: '#5347AA',
        strokeStyle: 'shortdash',
        strokeOpacity: 0.5
    });
});

// 5번 확진자
var polyline_5 = new naver.maps.Polyline({
    map: map,
    path: [
        new naver.maps.LatLng(37.461439, 126.447600),
        new naver.maps.LatLng(37.592164, 127.009733),
        new naver.maps.LatLng(37.563981, 127.029543),
        new naver.maps.LatLng(37.523686, 127.046616),
        new naver.maps.LatLng(37.589068, 127.092039),
        new naver.maps.LatLng(37.612687, 127.098255)
    ],
    clickable: true,
    strokeColor: '#5347AA',
    strokeStyle: 'shortdash',
    strokeOpacity: 0.5,
    strokeWeight: 5
});
var circle = new naver.maps.Circle({
    map: map,
    center: new naver.maps.LatLng(37.461439, 126.447600),
    radius: 1000,
    fillColor: '#F781F3',
    fillOpacity: 0.3
});
var circle = new naver.maps.Circle({
    map: map,
    center: new naver.maps.LatLng(37.592164, 127.009733),
    radius: 1000,
    fillColor: '#F781F3',
    fillOpacity: 0.3
});
var circle = new naver.maps.Circle({
    map: map,
    center: new naver.maps.LatLng(37.563981, 127.029543),
    radius: 1000,
    fillColor: '#F781F3',
    fillOpacity: 0.3
});
var circle = new naver.maps.Circle({
    map: map,
    center: new naver.maps.LatLng(37.523686, 127.046616),
    radius: 1000,
    fillColor: '#F781F3',
    fillOpacity: 0.3
});
var circle = new naver.maps.Circle({
    map: map,
    center: new naver.maps.LatLng(37.589068, 127.092039),
    radius: 1000,
    fillColor: '#F781F3',
    fillOpacity: 0.3
});
var circle = new naver.maps.Circle({
    map: map,
    center: new naver.maps.LatLng(37.612687, 127.098255),
    radius: 1000,
    fillColor: '#F781F3',
    fillOpacity: 0.3
});
naver.maps.Event.addListener(polyline_5, 'mouseover', function() {
    polyline_5.setOptions({
        strokeColor: '#F781F3',
        strokeStyle: 'solid',
        strokeOpacity: 1
    });
});
naver.maps.Event.addListener(polyline_5, 'mouseout', function() {
    polyline_5.setOptions({
        strokeColor: '#5347AA',
        strokeStyle: 'shortdash',
        strokeOpacity: 0.5
    });
});

// 6번 확진자
var polyline_6 = new naver.maps.Polyline({
    map: map,
    path: [
        new naver.maps.LatLng(37.527679, 127.032403),
        new naver.maps.LatLng(37.585234, 126.998814),
        new naver.maps.LatLng(37.578512, 126.997888),
    ],
    clickable: true,
    strokeColor: '#5347AA',
    strokeStyle: 'shortdash',
    strokeOpacity: 0.5,
    strokeWeight: 5
});
var circle = new naver.maps.Circle({
    map: map,
    center: new naver.maps.LatLng(37.527679, 127.032403),
    radius: 1000,
    fillColor: '#2EFEF7',
    fillOpacity: 0.3
});
var circle = new naver.maps.Circle({
    map: map,
    center: new naver.maps.LatLng(37.585234, 126.998814),
    radius: 1000,
    fillColor: '#2EFEF7',
    fillOpacity: 0.3
});
var circle = new naver.maps.Circle({
    map: map,
    center: new naver.maps.LatLng(37.578512, 126.997888),
    radius: 1000,
    fillColor: '#2EFEF7',
    fillOpacity: 0.3
});
naver.maps.Event.addListener(polyline_6, 'mouseover', function() {
    polyline_6.setOptions({
        strokeColor: '#2EFEF7',
        strokeStyle: 'solid',
        strokeOpacity: 1
    });
});
naver.maps.Event.addListener(polyline_6, 'mouseout', function() {
    polyline_6.setOptions({
        strokeColor: '#5347AA',
        strokeStyle: 'shortdash',
        strokeOpacity: 0.5
    });
});

// 7번 확진자
var polyline_7 = new naver.maps.Polyline({
    map: map,
    path: [
        new naver.maps.LatLng(37.461439, 126.447600),
        new naver.maps.LatLng(37.614380, 126.839901),
        new naver.maps.LatLng(37.612710, 127.097589),
    ],
    clickable: true,
    strokeColor: '#5347AA',
    strokeStyle: 'shortdash',
    strokeOpacity: 0.5,
    strokeWeight: 5
});
var circle = new naver.maps.Circle({
    map: map,
    center: new naver.maps.LatLng(37.461439, 126.447600),
    radius: 1000,
    fillColor: '#BCF5A9',
    fillOpacity: 0.3
});
var circle = new naver.maps.Circle({
    map: map,
    center: new naver.maps.LatLng(37.614380, 126.839901),
    radius: 1000,
    fillColor: '#BCF5A9',
    fillOpacity: 0.3
});
var circle = new naver.maps.Circle({
    map: map,
    center: new naver.maps.LatLng(37.612710, 127.097589),
    radius: 1000,
    fillColor: '#BCF5A9',
    fillOpacity: 0.3
});
naver.maps.Event.addListener(polyline_7, 'mouseover', function() {
    polyline_7.setOptions({
        strokeColor: '#BCF5A9',
        strokeStyle: 'solid',
        strokeOpacity: 1
    });
});
naver.maps.Event.addListener(polyline_7, 'mouseout', function() {
    polyline_7.setOptions({
        strokeColor: '#5347AA',
        strokeStyle: 'shortdash',
        strokeOpacity: 0.5
    });
});

// 8번째 확진자
var polyline_8 = new naver.maps.Polyline({
    map: map,
    path: [
        new naver.maps.LatLng(37.461439, 126.447600),
        new naver.maps.LatLng(37.489389, 127.014396),
        new naver.maps.LatLng(36.013037, 126.764139),
        new naver.maps.LatLng(35.986654, 126.708093),
        new naver.maps.LatLng(35.968097, 126.716211),
        new naver.maps.LatLng(35.954833, 126.712085),
        new naver.maps.LatLng(35.982612, 126.734876),
        new naver.maps.LatLng(35.964623, 126.958952),
    ],
    clickable: true,
    strokeColor: '#5347AA',
    strokeStyle: 'shortdash',
    strokeOpacity: 0.5,
    strokeWeight: 5
});
var circle = new naver.maps.Circle({
    map: map,
    center: new naver.maps.LatLng(37.461439, 126.447600),
    radius: 1000,
    fillColor: '#A4A4A4',
    fillOpacity: 0.3
});
var circle = new naver.maps.Circle({
    map: map,
    center: new naver.maps.LatLng(37.489389, 127.014396),
    radius: 1000,
    fillColor: '#A4A4A4',
    fillOpacity: 0.3
});
var circle = new naver.maps.Circle({
    map: map,
    center: new naver.maps.LatLng(36.013037, 126.764139),
    radius: 1000,
    fillColor: '#A4A4A4',
    fillOpacity: 0.3
});
var circle = new naver.maps.Circle({
    map: map,
    center: new naver.maps.LatLng(35.986654, 126.708093),
    radius: 1000,
    fillColor: '#A4A4A4',
    fillOpacity: 0.3
});
var circle = new naver.maps.Circle({
    map: map,
    center: new naver.maps.LatLng(35.968097, 126.716211),
    radius: 1000,
    fillColor: '#A4A4A4',
    fillOpacity: 0.3
});
var circle = new naver.maps.Circle({
    map: map,
    center: new naver.maps.LatLng(35.954833, 126.712085),
    radius: 1000,
    fillColor: '#A4A4A4',
    fillOpacity: 0.3
});
var circle = new naver.maps.Circle({
    map: map,
    center: new naver.maps.LatLng(35.982612, 126.734876),
    radius: 1000,
    fillColor: '#A4A4A4',
    fillOpacity: 0.3
});
var circle = new naver.maps.Circle({
    map: map,
    center: new naver.maps.LatLng(35.964623, 126.958952),
    radius: 1000,
    fillColor: '#A4A4A4',
    fillOpacity: 0.3
});
naver.maps.Event.addListener(polyline_8, 'mouseover', function() {
    polyline_8.setOptions({
        strokeColor: '#A4A4A4',
        strokeStyle: 'solid',
        strokeOpacity: 1
    });
});
naver.maps.Event.addListener(polyline_8, 'mouseout', function() {
    polyline_8.setOptions({
        strokeColor: '#5347AA',
        strokeStyle: 'shortdash',
        strokeOpacity: 0.5
    });
});

// 9번 확진자
var polyline_9 = new naver.maps.Polyline({
    map: map,
    path: [
        new naver.maps.LatLng(37.592639, 127.093739),
        new naver.maps.LatLng(37.612704, 127.097866),
    ],
    clickable: true,
    strokeColor: '#5347AA',
    strokeStyle: 'shortdash',
    strokeOpacity: 0.5,
    strokeWeight: 5
});
var circle = new naver.maps.Circle({
    map: map,
    center: new naver.maps.LatLng(37.592639, 127.093739),
    radius: 1000,
    fillColor: '#2E64FE',
    fillOpacity: 0.3
});
var circle = new naver.maps.Circle({
    map: map,
    center: new naver.maps.LatLng(37.612704, 127.097866),
    radius: 1000,
    fillColor: '#2E64FE',
    fillOpacity: 0.3
});
naver.maps.Event.addListener(polyline_9, 'mouseover', function() {
    polyline_9.setOptions({
        strokeColor: '#2E64FE',
        strokeStyle: 'solid',
        strokeOpacity: 1
    });
});
naver.maps.Event.addListener(polyline_9, 'mouseout', function() {
    polyline_9.setOptions({
        strokeColor: '#5347AA',
        strokeStyle: 'shortdash',
        strokeOpacity: 0.5
    });
});

// 10,11번 확진자
var polyline_10 = new naver.maps.Polyline({
    map: map,
    path: [
        new naver.maps.LatLng(37.642686, 126.788058),
        new naver.maps.LatLng(37.578631, 126.997718),
    ],
    clickable: true,
    strokeColor: '#5347AA',
    strokeStyle: 'shortdash',
    strokeOpacity: 0.5,
    strokeWeight: 5
});
var circle = new naver.maps.Circle({
    map: map,
    center: new naver.maps.LatLng(37.642686, 126.788058),
    radius: 1000,
    fillColor: '#DF0174',
    fillOpacity: 0.3
});
var circle = new naver.maps.Circle({
    map: map,
    center: new naver.maps.LatLng(37.578631, 126.997718),
    radius: 1000,
    fillColor: '#DF0174',
    fillOpacity: 0.3
});
naver.maps.Event.addListener(polyline_10, 'mouseover', function() {
    polyline_10.setOptions({
        strokeColor: '#DF0174',
        strokeStyle: 'solid',
        strokeOpacity: 1
    });
});
naver.maps.Event.addListener(polyline_10, 'mouseout', function() {
    polyline_10.setOptions({
        strokeColor: '#5347AA',
        strokeStyle: 'shortdash',
        strokeOpacity: 0.5
    });
});

// 12번 확진자
var polyline_12_1 = new naver.maps.Polyline({
    map: map,
    path: [
        new naver.maps.LatLng(37.559660, 126.803975),
        new naver.maps.LatLng(37.560387, 126.975541),
        new naver.maps.LatLng(37.484724, 126.782437),
        new naver.maps.LatLng(37.461602, 126.631519),
        new naver.maps.LatLng(37.484724, 126.782437),
        new naver.maps.LatLng(37.555178, 126.969823),
        new naver.maps.LatLng(37.763977, 128.898932),
        new naver.maps.LatLng(37.683358, 129.043706),
    ],
    clickable: true,
    strokeColor: '#5347AA',
    strokeStyle: 'shortdash',
    strokeOpacity: 0.5,
    strokeWeight: 5
});
var polyline_12_2 = new naver.maps.Polyline({
    map: map,
    path: [
        new naver.maps.LatLng(37.484724, 126.782437),
        new naver.maps.LatLng(37.266013, 126.999612),
        new naver.maps.LatLng(37.359087, 126.931228),
        new naver.maps.LatLng(37.484724, 126.782437),
        new naver.maps.LatLng(37.351316, 127.123325),
    ],
    clickable: true,
    strokeColor: '#5347AA',
    strokeStyle: 'shortdash',
    strokeOpacity: 0.5,
    strokeWeight: 5
});
var circle = new naver.maps.Circle({
    map: map,
    center: new naver.maps.LatLng(37.484724, 126.782437),
    radius: 3000,
    fillColor: '#0404B4',
    fillOpacity: 0.3
});
var circle = new naver.maps.Circle({
    map: map,
    center: new naver.maps.LatLng(37.560387, 126.975541),
    radius: 1000,
    fillColor: '#0404B4',
    fillOpacity: 0.3
});
var circle = new naver.maps.Circle({
    map: map,
    center: new naver.maps.LatLng(37.461602, 126.631519),
    radius: 1000,
    fillColor: '#0404B4',
    fillOpacity: 0.3
});
var circle = new naver.maps.Circle({
    map: map,
    center: new naver.maps.LatLng(37.555178, 126.969823),
    radius: 1000,
    fillColor: '#0404B4',
    fillOpacity: 0.3
});
var circle = new naver.maps.Circle({
    map: map,
    center: new naver.maps.LatLng(37.763977, 128.898932),
    radius: 1000,
    fillColor: '#0404B4',
    fillOpacity: 0.3
});
var circle = new naver.maps.Circle({
    map: map,
    center: new naver.maps.LatLng(37.683358, 129.043706),
    radius: 1000,
    fillColor: '#0404B4',
    fillOpacity: 0.3
});
var circle = new naver.maps.Circle({
    map: map,
    center: new naver.maps.LatLng(37.266013, 126.999612),
    radius: 3000,
    fillColor: '#0404B4',
    fillOpacity: 0.3
});
var circle = new naver.maps.Circle({
    map: map,
    center: new naver.maps.LatLng(37.359087, 126.931228),
    radius: 2000,
    fillColor: '#0404B4',
    fillOpacity: 0.3
});
var circle = new naver.maps.Circle({
    map: map,
    center: new naver.maps.LatLng(37.351316, 127.123325),
    radius: 1000,
    fillColor: '#0404B4',
    fillOpacity: 0.3
});
naver.maps.Event.addListener(polyline_12_1, 'mouseover', function() {
    polyline_12_1.setOptions({
        strokeColor: '#0404B4',
        strokeStyle: 'solid',
        strokeOpacity: 1
    });
    polyline_12_2.setOptions({
        strokeColor: '#0404B4',
        strokeStyle: 'solid',
        strokeOpacity: 1
    });
});
naver.maps.Event.addListener(polyline_12_1, 'mouseout', function() {
    polyline_12_1.setOptions({
        strokeColor: '#5347AA',
        strokeStyle: 'shortdash',
        strokeOpacity: 0.5
    });
    polyline_12_2.setOptions({
        strokeColor: '#5347AA',
        strokeStyle: 'shortdash',
        strokeOpacity: 0.5
    });
});
naver.maps.Event.addListener(polyline_12_2, 'mouseover', function() {
    polyline_12_1.setOptions({
        strokeColor: '#0404B4',
        strokeStyle: 'solid',
        strokeOpacity: 1
    });
    polyline_12_2.setOptions({
        strokeColor: '#0404B4',
        strokeStyle: 'solid',
        strokeOpacity: 1
    });
});
naver.maps.Event.addListener(polyline_12_2, 'mouseout', function() {
    polyline_12_1.setOptions({
        strokeColor: '#5347AA',
        strokeStyle: 'shortdash',
        strokeOpacity: 0.5
    });
    polyline_12_2.setOptions({
        strokeColor: '#5347AA',
        strokeStyle: 'shortdash',
        strokeOpacity: 0.5
    });
});

// 13번 확진자
var polyline_13 = new naver.maps.Polyline({
    map: map,
    path: [
        new naver.maps.LatLng(37.559660, 126.803975),
        new naver.maps.LatLng(37.567228, 127.005552),
    ],
    clickable: true,
    strokeColor: '#5347AA',
    strokeStyle: 'shortdash',
    strokeOpacity: 0.5,
    strokeWeight: 5
});
var circle = new naver.maps.Circle({
    map: map,
    center: new naver.maps.LatLng(37.559660, 126.803975),
    radius: 1000,
    fillColor: '#585858',
    fillOpacity: 0.3
});
var circle = new naver.maps.Circle({
    map: map,
    center: new naver.maps.LatLng(37.567228, 127.005552),
    radius: 1000,
    fillColor: '#585858',
    fillOpacity: 0.3
});
naver.maps.Event.addListener(polyline_13, 'mouseover', function() {
    polyline_13.setOptions({
        strokeColor: '#585858',
        strokeStyle: 'solid',
        strokeOpacity: 1
    });
});
naver.maps.Event.addListener(polyline_13, 'mouseout', function() {
    polyline_13.setOptions({
        strokeColor: '#5347AA',
        strokeStyle: 'shortdash',
        strokeOpacity: 0.5
    });
});

// TODO: 버튼을 누르면 선이 칠해짐.