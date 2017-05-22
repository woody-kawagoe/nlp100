<form action="/" method="get">
    アーティスト名: <input name="name" type="text" /></br>
    アーティストの別名: <input name="aliases_name" type="text" /></br>
    タグ: <input name="tags_value" type="text" /></br>
    <input value="送信", type="submit" />
</form>
<p>name:{{name}}</p>
<p>aliases_name:{{aliases_name}}</p>
<p>tags_value:{{tags_value}}</p>
% for a in sorted(result, key=lambda x:x['id']):
<h1>{{a['name']}}</h1>
%   for k in a.keys():
<p>{{k}}:{{a[k]}}</p>
%   end
% end
