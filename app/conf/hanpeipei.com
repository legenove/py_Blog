upstream my_blog {
    server 127.0.0.1:21000 fail_timeout=0;
    server 127.0.0.1:21001 fail_timeout=0;
    server 127.0.0.1:21002 fail_timeout=0;
    server 127.0.0.1:21003 fail_timeout=0;
    server 127.0.0.1:21004 fail_timeout=0;
    server 127.0.0.1:21005 fail_timeout=0;
    server 127.0.0.1:21006 fail_timeout=0;
    server 127.0.0.1:21007 fail_timeout=0;
}

server {
    listen 80;
#    server_name app.cms.m.youku.com;
    charset utf-8;

    location /static/ {
        alias /opt/app/python/py_Blog/app/contents/static/;
    }

    location / {
#        proxy_pass  http://my_blog;
#        proxy_connect_timeout 3;
#        proxy_send_timeout 3;
#        proxy_read_timeout 3;
#        proxy_redirect      default;
#         #  proxy_set_header    X-Forwarded-For $proxy_add_x_forwarded_for;
#          # proxy_set_header    X-Real-IP $x_remote_addr;
#        proxy_set_header    Host $http_host;
#        proxy_set_header    Range $http_range;
#        # 只允许内网访问
#        allow 60.247.104.99; # 办公室的公网IP
#        allow 211.157.171.226;
#        allow 10.10.0.0/16;
#        allow 10.10.116.0/24;
#        allow 10.10.202.0/24;
#        allow 218.30.0.0/16;
#        allow 10.9.0.0/16; #上海网段
#        allow 10.155.0.0/16; #理想
#        deny all;
        fastcgi_pass my_blog;
        fastcgi_param PATH_INFO $fastcgi_script_name;
        fastcgi_param REQUEST_METHOD $request_method;
        fastcgi_param QUERY_STRING $query_string;
        fastcgi_param SERVER_NAME $server_name;
        fastcgi_param SERVER_PORT $server_port;
        fastcgi_param SERVER_PROTOCOL $server_protocol;
        fastcgi_param CONTENT_TYPE $content_type;
        fastcgi_param CONTENT_LENGTH $content_length;
        fastcgi_pass_header Authorization;
        fastcgi_intercept_errors off;
    }

}