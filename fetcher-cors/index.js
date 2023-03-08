import axios from "axios"

const url = "https://finishershub-backend.vercel.app/api/registry"
const localUrl = "http://localhost:3000/api/registry"

const testRegistryFetch = (url) => {
  axios
    .get(url)
    .then((res) => res.data)
    .then((data) => console.log(data))
}

testRegistryFetch(localUrl)
