import axios from 'axios';
import AppConfig from 'config/config';
axios.defaults.baseURL = AppConfig.baseURL;

export function submitFeedback(data: FormData) {
  return axios({
    data,
    method: 'post',
    url: '/api/mail/v0/feedback',
    headers: { 'Content-Type': 'multipart/form-data' },
  });
};
