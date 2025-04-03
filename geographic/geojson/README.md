# GeoJSON 형식

## 들어가기 전에
GeoJson은 JSON을 기반으로 하는 지리 공간 데이터 교환 형식이다. 여러 유형의 JSON 객체를 결합하여 **지리적 특징**, **속성 및 공간적 범위**에 대한 데이터를 표현하는 방식을 정의한다. 참고로 GeoJSON은 WGS(World Geodeetic System) 1984 좌표계와 십진수를 사용한다.

## 개요
위에서 설명했듯이, GeoJSON은 다양한 지리 정보를 JSON 구조를 이용해 구조화 한 것이다. GeoJSON은 공간의 위치 (Geometry), 부분적인 지리 공간[원문: spatially [bounded](https://ko.wikipedia.org/wiki/%EC%9C%A0%EA%B3%84_%EC%A7%91%ED%95%A9) entity] (a Feature), 여러 부분적인 지리 공간들을 표현할 수 있다[원문: a list of Features] (a FeatureCollection). GeoJSON은 Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon, GeomtryCollectino과 같은 타입들을 지원한다. GeoJSON에서의 Feature는 Geometry 객체와 추가적인 속성들을 포함하며, FeatureColleciton은 여러 개의 Feature를 가진다.

해당 형식은 가장 넓은 지리학 정보를 고려하여 만들어졌다. 지리적 공간에 존재하는 모든 것들은 물리적 구조체가 아니더라도 특징(Feature)이 될 수 있다. GeoJSON의 개념은 새로운 것이 아니고, 지리학 정보 표준 시스템과 
JSON을 이용한 웹 애플리케이션 개발에 최적화에서 파생되어 생긴 것 이다.


GeoJSON은 기존에 SFSQL[OpenGIS Simple Features Implementation Specification for SQL]에서 정의된 7개의 지리학 타입들을 통해서 구성됐다. 
- 0 차원(점): Point, MultiPoint
- 1 차원(선): LineString, MultiLineString
- 2 차원(면): Polygon, MultiPolygon, GeometryCollection[heterogeneous:  이질의]

GeoJSON에서 제공하는 기하학적 객체들은 [WKB](http://ww다.gisdeveloper.co.kr/?p=997#:~:text=WKB%2C%20%EC%A6%89%20Well%2Dknown%20Binary%EB%8A%94%20OpenGIS%20%EC%8A%A4%ED%8E%99%EC%97%90%20%EC%9D%98%ED%95%B4,%EC%A7%80%EC%98%A4%EB%A9%94%ED%8A%B8%EB%A6%AC%20WKB%20%EC%A0%95%EB%B3%B4%EB%A5%BC%20%EB%8B%B4%EA%B3%A0%20%EC%9E%88%EB%8A%94%20BLOB%20%ED%83%80%EC%9E%85)와 [WKT](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry)와 유사하다.

GeoJSON 또한 Feature와 FeatureCollection을 구성했고, GeoJSON에서의 Feature 객체들은 위에서 언급했던 기하학 타입들과 추가적인 것들을 포괄한다. FeactureCollection 객체는 Feature 객체들의 배열을 포함하고 있다. 이 구조는 Web Feature Service(WFS)이 [WFSv1]에 명시된 GetFeatures 요청 또는, Placemarks[KMLv.2.2]의 Keyhole Markup Langauge[KML] 폴더 구조에 응답하는 것과 유사하다. WFS 사양에 대한 구현체 또한, GetFeature 요청에 대한 GeoJSON 형식의 응답을 제공한다. 그러나 일부 WFS(Web Feature Service) 구현에서는 GetFeature 요청에 대한 응답을 GeoJSON 형식으로 제공하기도 하지만, GeoJSON 자체는 특정한 서비스 모델이나 Feature 타입의 개념 체계를 강제하지 않는다. 이것이 최초로 공개된 2008년 이래로, GeoJSON 형식의 사양이다유명해졌다. JavaScript web-mappling 라이브러리들, JSON 기반의 Document 데이터베이스들과 Web API들에서 널리 사용되기 시작했다.
 
---
참고
- 해당 번역본은 학습을 위한 개인적인 번역입니다.
- 해당 문서의 모든 저작권은 IETF에게 있습니다.