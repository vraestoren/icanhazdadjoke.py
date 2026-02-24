from requests import Session

class Icanhazdadjoke:
	def __init__(self) -> None:
		self.api = "https://icanhazdadjoke.com"
		self.session = Session()
		self.session.headers = {
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
			"Accept": "application/json"
		}
	
	def get_random_dad_joke(self) -> dict:
		return self.session.get(self.api).json()
	
	def get_random_dad_joke_as_slack(self) -> dict:
		return self.session.get(
			f"{self.api}/slack").json()
	
	def get_dad_joke(self, joke_id: str) -> dict:
		return self.session.get(f"{self.api}/j/{joke_id}").json()
	
	def get_dad_joke_as_image(self, joke_id: str) -> str:
		return f"{self.api}/j/{joke_id}.png"
	
	def search_dad_jokes(
			self,
			page: int = 1,
			limit: int = 20, # max = 30
			term: str = "list all jokes") -> dict:
		return self.session.get(
			f"{self.api}/search?page={page}&limit={limit}&term={term}").json()
