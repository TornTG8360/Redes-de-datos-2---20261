import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
  vus: 5,        // 5 usuarios virtuales
  duration: '10s', // 10 segundos
};

export default function () {
  let response = http.get('https://httpbin.org/delay/1');
  check(response, {
    'status es 200': (r) => r.status === 200,
  });
  sleep(1);
}
